#!/usr/bin/env python3
"""
ASX 50 climate disclosure quality: analysis.

Structured around four descriptive questions:
  Q1  What is the overall level and shape of the score distribution?
  Q2  Is disclosure quality even across the TCFD framework?
  Q3  Do differences track company characteristics (size, climate exposure)?
  Q4  Where are disclosure score gaps concentrated?

Everything here is descriptive. Nothing supports a causal claim: one year,
n = 50, no instrument, no panel.

Usage:
    pip install -r requirements.txt
    python analysis.py [workbook.xlsx]

Outputs:
    results/   CSV tables
    figures/   PDF and PNG figures
"""

from __future__ import annotations

import argparse
import hashlib
import platform
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy import stats

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_WORKBOOK = BASE_DIR / "asx50_coding_workbook_v2_2_auditable.xlsx"
RESULTS = BASE_DIR / "results"
FIGURES = BASE_DIR / "figures"

ITEMS = ["G_a", "G_b", "S_a", "S_b", "S_c", "R_a", "R_b", "R_c", "M_a", "M_b", "M_c"]
PILLAR = {"G_a": "Governance", "G_b": "Governance",
          "S_a": "Strategy", "S_b": "Strategy", "S_c": "Strategy",
          "R_a": "Risk Mgmt", "R_b": "Risk Mgmt", "R_c": "Risk Mgmt",
          "M_a": "Metrics & Targets", "M_b": "Metrics & Targets", "M_c": "Metrics & Targets"}
PILLAR_ORDER = ["Governance", "Strategy", "Risk Mgmt", "Metrics & Targets"]
MAX_ITEM, MAX_TOTAL = 2, 22

# --------------------------------------------------------------------------
# Climate exposure grouping.
#
# Groups companies by the TYPE of climate-related exposure their principal
# business creates, not by how much they emit. GICS sectors are not used
# directly: five of the eleven GICS sectors contain only two companies each,
# so sector means would be unstable.
#
# Reference is not a low-exposure "sector". It is a residual category holding
# companies that fit none of the three exposure types. It is internally
# heterogeneous (software, biotech, gaming, retail, telecoms) and exists to
# give the regression a baseline, not to describe a real industry.
#
# Every assignment below is a judgement and is documented in codebook.md.
# --------------------------------------------------------------------------
EXPOSURE = {
    # Transition: revenue tied to emissions-intensive activity; exposed to
    # carbon pricing, policy and technology substitution.
    **{t: "Transition" for t in
       ["BHP", "BSL", "EVN", "FMG", "JHX", "LYC", "NEM", "NST", "PLS", "RIO", "S32",
        "STO", "WDS",
        "ORG", "APA",
        "QAN"]},
    # Physical: assets fixed in place or supply chains exposed to acute and
    # chronic weather.
    **{t: "Physical" for t in
       ["GPT", "SGP", "GMG", "SCG",
        "TCL",
        "COL", "WOW",
        "BXB"]},
    # Indirect: little own emissions; exposure runs through lending,
    # underwriting and investment portfolios (financed emissions).
    **{t: "Indirect" for t in
       ["ANZ", "CBA", "NAB", "WBC", "ASX", "MQG", "SOL", "IAG", "QBE", "SUN"]},
    # Reference: residual.
    **{t: "Reference" for t in
       ["TLS", "CAR", "WES", "ALL", "LNW", "TLC",
        "CSL", "COH", "RMD", "SHL", "SIG", "MPL",
        "ALQ", "CPU", "WTC", "XRO"]},
}
GROUP_ORDER = ["Transition", "Physical", "Indirect", "Reference"]
SMALL_GROUP = 10

COLOURS = {"Governance": "#3d5a80", "Strategy": "#98c1d9",
           "Risk Mgmt": "#ee6c4d", "Metrics & Targets": "#293241"}

# Okabe-Ito, colourblind safe. Reference is grey because it is a residual
# category, not a substantive group.
GROUP_COLOUR = {"Transition": "#D55E00", "Physical": "#0072B2",
                "Indirect": "#009E73", "Reference": "#999999"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Reproduce the ASX 50 FY2025 climate-disclosure analysis."
    )
    parser.add_argument(
        "workbook",
        nargs="?",
        default=str(DEFAULT_WORKBOOK),
        help="Path to the audited coding workbook.",
    )
    return parser.parse_args()


# ======================================================================= load


def require_columns(df: pd.DataFrame, required: set[str], sheet: str) -> None:
    missing = sorted(required - set(df.columns))
    if missing:
        raise SystemExit(f"Sheet '{sheet}' is missing required columns: {missing}")


def audit_sources(df: pd.DataFrame, sources: pd.DataFrame) -> None:
    """Verify that every company-item score has one auditable source record."""
    required = {"ticker", "item", "score", "document", "page", "note"}
    require_columns(sources, required, "Sources")

    sources["ticker"] = sources["ticker"].astype(str).str.strip().str.upper()
    sources["item"] = sources["item"].astype(str).str.strip()

    duplicates = sources.duplicated(["ticker", "item"], keep=False)
    if duplicates.any():
        bad = sources.loc[duplicates, ["ticker", "item"]]
        raise SystemExit("Duplicate ticker-item rows found in Sources:\n"
                         + bad.to_string(index=False))

    expected = pd.MultiIndex.from_product(
        [df["ticker"].tolist(), ITEMS], names=["ticker", "item"]
    )
    actual = pd.MultiIndex.from_frame(sources[["ticker", "item"]])
    missing = expected.difference(actual)
    extra = actual.difference(expected)

    if len(missing):
        raise SystemExit("Missing source records:\n" + "\n".join(
            f"{ticker}, {item}" for ticker, item in missing
        ))
    if len(extra):
        raise SystemExit("Unexpected source records:\n" + "\n".join(
            f"{ticker}, {item}" for ticker, item in extra
        ))

    for column in ["document", "page", "note"]:
        blank = (sources[column].isna()
                 | sources[column].astype(str).str.strip().eq(""))
        if blank.any():
            bad = sources.loc[blank, ["ticker", "item"]]
            raise SystemExit(f"Blank '{column}' values found in Sources:\n"
                             + bad.to_string(index=False))

    source_scores = pd.to_numeric(sources["score"], errors="coerce")
    if source_scores.isna().any():
        raise SystemExit("Non-numeric scores found in Sources.")
    if (~source_scores.isin([0, 1, 2])).any():
        raise SystemExit("Sources contains scores outside the permitted 0-2 range.")
    source_scores = source_scores.astype(int)

    workbook_scores = df.set_index("ticker")[ITEMS].stack()
    workbook_scores.index.names = ["ticker", "item"]
    observed = pd.Series(source_scores.to_numpy(), index=actual)
    expected_scores = workbook_scores.reindex(actual)
    mismatch = observed != expected_scores
    if mismatch.any():
        rows = []
        for (ticker, item), score in observed[mismatch].items():
            rows.append({
                "ticker": ticker,
                "item": item,
                "sources_score": int(score),
                "scores_sheet_score": int(workbook_scores.loc[(ticker, item)]),
            })
        raise SystemExit("Scores disagree between Scores and Sources:\n"
                         + pd.DataFrame(rows).to_string(index=False))

    expected_rows = len(df) * len(ITEMS)
    print(f"Source audit passed: {len(sources)}/{expected_rows} "
          "company-item records are complete and consistent.")


def load(path: Path):
    if not path.exists():
        raise SystemExit(f"Workbook not found: {path}")

    scores = pd.read_excel(path, sheet_name="Scores")
    companies = pd.read_excel(path, sheet_name="Companies")
    sources = pd.read_excel(path, sheet_name="Sources")

    require_columns(scores, {"ticker", "company", "total", *ITEMS}, "Scores")
    require_columns(companies, {
        "ticker", "company", "gics_sector", "index_weight_pct",
        "report_location", "domicile", "aasb_s2_applies",
    }, "Companies")

    for df in (scores, companies, sources):
        df.dropna(subset=["ticker"], inplace=True)
        df["ticker"] = df["ticker"].astype(str).str.strip().str.upper()
        df.drop(df[df["ticker"] == "EXAMPLE"].index, inplace=True)

    df = companies.merge(scores.drop(columns=["company"]), on="ticker", validate="1:1")
    numeric_scores = df[ITEMS].apply(pd.to_numeric, errors="coerce")
    if numeric_scores.isna().any().any():
        raise SystemExit("Blank or non-numeric item scores found in Scores.")
    if (~numeric_scores.isin([0, 1, 2])).any().any():
        raise SystemExit("Scores contains values outside the permitted 0-2 range.")
    df[ITEMS] = numeric_scores.astype(int)
    df["total"] = df[ITEMS].sum(axis=1)
    df["exposure"] = df["ticker"].map(EXPOSURE)

    if df["index_weight_pct"].isna().any():
        raise SystemExit("Missing index_weight_pct values found.")
    if (df["index_weight_pct"] <= 0).any():
        raise SystemExit("index_weight_pct must be greater than zero.")

    df["log_weight"] = np.log10(df["index_weight_pct"])
    for p in PILLAR_ORDER:
        df[p] = df[[i for i in ITEMS if PILLAR[i] == p]].mean(axis=1)

    unmapped = df.loc[df["exposure"].isna(), "ticker"].tolist()
    if unmapped:
        raise SystemExit(f"Tickers missing from EXPOSURE map: {unmapped}")
    if len(df) != 50:
        raise SystemExit(f"Expected 50 companies, found {len(df)}")
    if ((df[ITEMS] < 0) | (df[ITEMS] > MAX_ITEM)).any().any():
        raise SystemExit("Scores outside 0-2 found")
    print(f"Loaded {len(df)} companies. Exposure groups: "
          f"{df['exposure'].value_counts().reindex(GROUP_ORDER).to_dict()}")
    return df, sources


# ================================================== Q1 level and distribution


def q1_distribution(df: pd.DataFrame) -> pd.Series:
    t = df["total"]
    out = pd.Series({
        "n": len(t), "possible_max": MAX_TOTAL,
        "mean": t.mean(), "median": t.median(), "sd": t.std(ddof=1),
        "min": t.min(), "max": t.max(),
        "iqr": t.quantile(.75) - t.quantile(.25),
        "pct_of_maximum": t.mean() / MAX_TOTAL * 100,
        "at_ceiling": int((t == MAX_TOTAL).sum()),
        "at_floor": int((t == 0).sum()),
        "skewness": stats.skew(t), "excess_kurtosis": stats.kurtosis(t),
        "shapiro_p": stats.shapiro(t).pvalue,
    })
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(t, bins=range(0, MAX_TOTAL + 2), color="#3d5a80", edgecolor="white")
    ax.axvline(t.mean(), color="#ee6c4d", ls="--", label=f"mean {t.mean():.1f}")
    ax.axvline(t.median(), color="#ee6c4d", ls=":", label=f"median {t.median():.1f}")
    ax.set_xlabel(f"Total disclosure score (0 to {MAX_TOTAL})")
    ax.set_ylabel("Companies")
    ax.set_title("Q1  Distribution of TCFD disclosure scores, ASX 50, FY2025")
    ax.legend(frameon=False)
    save(fig, "q1_distribution.png")
    return out


# =========================================== Q2 evenness across the framework


def q2_framework(df: pd.DataFrame):
    items = pd.DataFrame([{
        "item": i, "pillar": PILLAR[i],
        "mean": df[i].mean(), "sd": df[i].std(ddof=1),
        "n_0": int((df[i] == 0).sum()), "n_1": int((df[i] == 1).sum()),
        "n_2": int((df[i] == 2).sum()), "pct_at_2": (df[i] == 2).mean() * 100,
    } for i in ITEMS])

    pillars = pd.DataFrame([{
        "pillar": p, "n_items": sum(1 for i in ITEMS if PILLAR[i] == p),
        "mean_per_item": df[p].mean(), "sd": df[p].std(ddof=1),
        "pct_of_maximum": df[p].mean() / MAX_ITEM * 100,
    } for p in PILLAR_ORDER]).sort_values("mean_per_item")

    chi2, p = stats.friedmanchisquare(*[df[i] for i in ITEMS])
    pillars.attrs["friedman"] = (f"Friedman chi2 = {chi2:.1f}, p = {p:.2e} "
                                 "(items differ from one another)")

    order = items.sort_values("mean")["item"].tolist()
    fig, ax = plt.subplots(figsize=(7.5, 5))
    left = np.zeros(len(order))
    for score, colour, label in [(0, "#c9c9c9", "0  not disclosed"),
                                 (1, "#98c1d9", "1  general"),
                                 (2, "#3d5a80", "2  specific")]:
        vals = np.array([(df[i] == score).sum() for i in order])
        ax.barh(order, vals, left=left, color=colour, label=label)
        left += vals
    for y, i in enumerate(order):
        ax.text(51, y, f"{df[i].mean():.2f}", va="center", fontsize=8, color="#555")
    ax.set_xlim(0, 58)
    ax.set_xlabel("Companies")
    ax.set_title("Q2  Score composition by recommended disclosure\n"
                 "(ordered by mean, shown at right)", fontsize=10)
    ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper center",
              bbox_to_anchor=(0.5, -0.12))
    save(fig, "q2_item_composition.png")
    return items, pillars


# ========================================= Q3 association with characteristics


def ols(y, X, names):
    """Plain OLS with t tests. statsmodels is not assumed to be installed."""
    X = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = len(y) - X.shape[1]
    se = np.sqrt(np.diag((resid @ resid / dof) * np.linalg.inv(X.T @ X)))
    t = beta / se
    p = 2 * (1 - stats.t.cdf(np.abs(t), dof))
    r2 = 1 - (resid @ resid) / ((y - y.mean()) ** 2).sum()
    out = pd.DataFrame({"term": ["intercept"] + names, "coef": beta,
                        "se": se, "t": t, "p_value": p})
    out.attrs["r2"] = r2
    out.attrs["adj_r2"] = 1 - (1 - r2) * (len(y) - 1) / dof
    return out


def q3_characteristics(df: pd.DataFrame):
    out = {}

    rho, p_rho = stats.spearmanr(df["index_weight_pct"], df["total"])
    r, p_r = stats.pearsonr(df["log_weight"], df["total"])
    out["size"] = pd.DataFrame([
        {"test": "Spearman rho, weight vs total", "statistic": rho, "p_value": p_rho,
         "note": "preferred: weight is skewed and scores are ordinal"},
        {"test": "Pearson r, log10(weight) vs total", "statistic": r, "p_value": p_r,
         "note": "index weight proxies float-adjusted market cap, not market cap"},
    ])

    pattern = df.groupby("exposure")[ITEMS].mean().reindex(GROUP_ORDER)
    out["exposure_item_pattern"] = pattern.round(3).reset_index()

    grp = df.groupby("exposure")["total"]
    totals = pd.DataFrame({"n": grp.size(), "mean": grp.mean(), "median": grp.median(),
                           "sd": grp.std(ddof=1), "min": grp.min(), "max": grp.max(),
                           "mean_log_weight": df.groupby("exposure")["log_weight"].mean()})
    totals = totals.reindex(GROUP_ORDER).reset_index()
    totals["underpowered"] = np.where(totals["n"] < SMALL_GROUP, "yes", "no")
    h, p_h = stats.kruskal(*[g["total"].to_numpy() for _, g in df.groupby("exposure")])
    totals.attrs["kruskal"] = f"Kruskal-Wallis H = {h:.2f}, p = {p_h:.4f}"
    out["exposure_totals"] = totals

    dummies = pd.get_dummies(df["exposure"]).reindex(columns=GROUP_ORDER)
    non_ref = [g for g in GROUP_ORDER if g != "Reference"]
    X = np.column_stack([df["log_weight"].to_numpy(dtype=float)] +
                        [dummies[g].to_numpy(dtype=float) for g in non_ref])
    model = ols(df["total"].to_numpy(dtype=float), X,
                ["log10_weight"] + [f"{g} vs Reference" for g in non_ref])
    model.attrs["note"] = (f"R2 = {model.attrs['r2']:.3f}, adj R2 = "
                           f"{model.attrs['adj_r2']:.3f}, n = {len(df)}. Descriptive only: "
                           "low powered, and exposure group correlates with size.")
    out["exposure_controlling_size"] = model

    for col in ["report_location", "domicile", "aasb_s2_applies"]:
        if col in df.columns and not df[col].isna().all():
            g = df.dropna(subset=[col]).groupby(col)["total"]
            out[f"meta_{col}"] = pd.DataFrame(
                {"n": g.size(), "mean": g.mean(), "sd": g.std(ddof=1)}).reset_index()
        else:
            print(f"  skipped '{col}': not yet populated in the Companies sheet")

    robust = size_tertile_robustness(df)
    out["exposure_robustness_tertiles"] = robust

    fig_q3(df, model, robust)
    fig_q3_item_pattern(df, pattern)
    return out


def size_tertile_robustness(df: pd.DataFrame) -> pd.DataFrame:
    """Replace continuous size with tertile dummies.

    A different functional form for the same control. If the exposure
    coefficients hold their sign and rough magnitude, the result is not an
    artefact of assuming a log-linear size effect.
    """
    d = df.copy()
    d["size_tertile"] = pd.qcut(d["log_weight"], 3, labels=["small", "mid", "large"])
    tert = pd.get_dummies(d["size_tertile"])
    dummies = pd.get_dummies(d["exposure"]).reindex(columns=GROUP_ORDER)
    non_ref = [g for g in GROUP_ORDER if g != "Reference"]
    X = np.column_stack([tert["mid"].to_numpy(float), tert["large"].to_numpy(float)]
                        + [dummies[g].to_numpy(float) for g in non_ref])
    model = ols(d["total"].to_numpy(float), X,
                ["mid tertile vs small", "large tertile vs small"]
                + [f"{g} vs Reference" for g in non_ref])
    model.attrs["note"] = (f"R2 = {model.attrs['r2']:.3f}, "
                           f"adj R2 = {model.attrs['adj_r2']:.3f}. "
                           "Robustness check: size entered as tertiles, not log-linear.")
    return model


def add_ci(model: pd.DataFrame, n: int) -> pd.DataFrame:
    """95 percent confidence intervals from the fitted t distribution."""
    dof = n - len(model)
    crit = stats.t.ppf(0.975, dof)
    out = model.copy()
    out["ci_low"] = out["coef"] - crit * out["se"]
    out["ci_high"] = out["coef"] + crit * out["se"]
    return out


def fig_q3(df: pd.DataFrame, model: pd.DataFrame, robust: pd.DataFrame) -> None:
    """Two panels: the size relationship, and the coefficients with intervals."""
    main = add_ci(model, len(df))
    rob = add_ci(robust, len(df))

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4),
                             gridspec_kw={"width_ratios": [1, 1.15]})

    # (a) size relationship
    ax = axes[0]
    for g in GROUP_ORDER:
        s = df[df["exposure"] == g]
        ax.scatter(s["index_weight_pct"], s["total"], s=44, alpha=.85,
                   color=GROUP_COLOUR[g], edgecolor="white", linewidth=.6,
                   label=f"{g} (n={len(s)})")
    xs = np.linspace(df["log_weight"].min(), df["log_weight"].max(), 50)
    slope, inter = np.polyfit(df["log_weight"], df["total"], 1)
    ax.plot(10 ** xs, inter + slope * xs, color="#000000", lw=1.2, ls="--", zorder=0)
    rho, p = stats.spearmanr(df["index_weight_pct"], df["total"])
    ax.set_xscale("log")
    ax.set_xlabel("Index weight, % (log scale)")
    ax.set_ylabel("Total disclosure score (0 to 22)")
    ax.set_ylim(0, 23)
    ax.set_title(f"(a)  Score against size\nSpearman rho = {rho:.2f}, p = {p:.3f}",
                 fontsize=10, loc="left")
    ax.legend(frameon=False, fontsize=7.5, loc="lower right")

    # (b) coefficients with 95% CI. Black: size entered as continuous log10
    # weight. Grey: the same models with size entered as tertiles, shown as a
    # robustness check.
    ax = axes[1]
    terms = [t for t in main["term"] if t != "intercept"]
    labels = {"log10_weight": "Size (log10 index weight)",
              "Transition vs Reference": "Transition vs Reference",
              "Physical vs Reference": "Physical vs Reference",
              "Indirect vs Reference": "Indirect vs Reference"}
    ypos = np.arange(len(terms))[::-1]
    for y, term in zip(ypos, terms):
        r = main[main["term"] == term].iloc[0]
        ax.plot([r.ci_low, r.ci_high], [y, y], color="#000000", lw=1.4)
        ax.plot(r.coef, y, "o", ms=7, color="#000000", zorder=3)
        robust_term = "large tertile vs small" if term == "log10_weight" else term
        rr = rob[rob["term"] == robust_term]
        if len(rr):
            rr = rr.iloc[0]
            ax.plot([rr.ci_low, rr.ci_high], [y - .26, y - .26], color="#999999", lw=1.2)
            ax.plot(rr.coef, y - .26, "s", ms=5, color="#999999", zorder=3)
    ax.axvline(0, color="#D55E00", lw=1, ls="--")
    ax.set_yticks(ypos, [labels.get(t, t) for t in terms], fontsize=8.5)
    ax.set_xlabel("Change in total score (points, out of 22)")
    ax.set_title("(b)  OLS coefficients, 95% confidence intervals\n"
                 "black: size as log10 weight   grey: size as tertiles",
                 fontsize=10, loc="left")
    ax.set_ylim(-0.7, len(terms) - 0.3)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.annotate("0 = no difference", xy=(0, -0.55), xytext=(0.35, -0.55),
                fontsize=7.5, color="#D55E00", va="center",
                arrowprops=dict(arrowstyle="->", color="#D55E00", lw=.8))

    fig.suptitle("Q3  Disclosure score, company size and climate exposure "
                 f"(n = {len(df)})", fontsize=11, y=1.04, x=0.01, ha="left")
    n_ref = int((df["exposure"] == "Reference").sum())
    fig.text(0.01, -0.10,
             "Baseline group (n = %d): companies whose principal business creates no "
             "concentrated climate exposure, comprising software, biotechnology, medical\n"
             "devices, gaming, professional services, telecommunications and retail. It is a "
             "residual category, not a benchmark, and is internally heterogeneous. In dummy\n"
             "coding one group must be omitted, and every coefficient in panel (b) is read "
             "against it: positive means higher than the baseline at the same company size.\n"
             "The choice of baseline is arbitrary and does not change model fit or predicted "
             "scores. Black markers hold size constant as log10 index weight; grey markers "
             "repeat the model with size as tertiles (small, mid, large), a robustness\n"
             "check on how size is measured. In the lower three rows black and grey estimate "
             "the same quantity. In the top row they do not: black is the change per tenfold "
             "increase in weight, grey is the largest tertile against the smallest." % n_ref,
             fontsize=7.2, color="#444444", ha="left", va="top", linespacing=1.5)
    save(fig, "q3_size_and_exposure")


def fig_q3_item_pattern(df: pd.DataFrame, pattern: pd.DataFrame) -> None:
    """Mean score by item and exposure group. Not affected by the size confound."""
    fig, ax = plt.subplots(figsize=(8.5, 3.4))
    heat = pattern[ITEMS].to_numpy(dtype=float)
    im = ax.imshow(heat, cmap="Blues", vmin=0, vmax=MAX_ITEM, aspect="auto")
    counts = df["exposure"].value_counts().reindex(GROUP_ORDER)
    ax.set_xticks(range(len(ITEMS)), ITEMS, fontsize=8.5)
    ax.set_yticks(range(len(GROUP_ORDER)),
                  [f"{g}  (n={counts[g]})" for g in GROUP_ORDER], fontsize=9)
    for i in range(heat.shape[0]):
        for j in range(heat.shape[1]):
            ax.text(j, i, f"{heat[i, j]:.1f}", ha="center", va="center", fontsize=7.5,
                    color="white" if heat[i, j] > 1.2 else "#222222")
    ax.set_title("Q3 supplementary  Unadjusted mean score by recommended disclosure "
                 "and exposure group\nDescriptive comparison only; these means do not "
                 "control for company size", fontsize=9.5, loc="left")
    fig.colorbar(im, ax=ax, shrink=.85, label="mean score (0 to 2)")
    save(fig, "q3_supp_item_pattern")


# ========================================== Q4 concentration of score gaps


def q4_score_gaps(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise observed score gaps without inferring content from prose notes.

    The evidence notes are intentionally company-specific natural language.
    They support human audit but are not a structured missing-element field.
    """
    rows = []
    for item in ITEMS:
        scores = df[item]
        points_lost = int((MAX_ITEM - scores).sum())
        rows.append({
            "item": item,
            "pillar": PILLAR[item],
            "mean_score": scores.mean(),
            "n_score_0": int((scores == 0).sum()),
            "n_score_1": int((scores == 1).sum()),
            "n_score_2": int((scores == 2).sum()),
            "n_below_maximum": int((scores < MAX_ITEM).sum()),
            "pct_below_maximum": (scores < MAX_ITEM).mean() * 100,
            "points_lost": points_lost,
            "pct_possible_points_lost": points_lost / (MAX_ITEM * len(scores)) * 100,
        })

    gaps = (pd.DataFrame(rows)
            .sort_values(["points_lost", "n_below_maximum"], ascending=False)
            .reset_index(drop=True))
    plot_data = gaps.sort_values("points_lost", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(plot_data["item"], plot_data["points_lost"],
            color=[COLOURS[p] for p in plot_data["pillar"]])
    for y, value in enumerate(plot_data["points_lost"]):
        ax.text(value + 0.5, y, str(value), va="center", fontsize=8, color="#555555")
    ax.set_xlabel("Score points below the maximum")
    ax.set_ylabel("Recommended disclosure")
    ax.set_title("Q4  Concentration of disclosure score gaps\n"
                 "Points lost relative to a maximum score of 2 per company")
    save(fig, "q4_score_gaps")
    return gaps


# ================================================================ reliability


def reliability(df: pd.DataFrame):
    x = df[ITEMS].to_numpy(dtype=float)
    k = x.shape[1]
    alpha = (k / (k - 1)) * (1 - x.var(axis=0, ddof=1).sum() / x.sum(axis=1).var(ddof=1))
    rows = []
    for i in ITEMS:
        rest = df[[j for j in ITEMS if j != i]].sum(axis=1)
        rho = np.nan if df[i].std(ddof=1) == 0 else stats.spearmanr(df[i], rest).statistic
        rows.append({"item": i, "pillar": PILLAR[i], "corrected_item_total_rho": rho})
    return alpha, pd.DataFrame(rows).sort_values("corrected_item_total_rho")


# ====================================================================== utils


def save(fig, name: str) -> None:
    """Write PDF for publication and PNG for slides and LinkedIn."""
    for ax in fig.axes:
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
    fig.tight_layout()
    stem = name[:-4] if name.endswith(".png") else name
    for ext in ("pdf", "png"):
        fig.savefig(FIGURES / f"{stem}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {FIGURES / stem}.pdf and .png")


def show(title: str, obj) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")
    if isinstance(obj, pd.Series):
        print(obj.round(3).to_string())
    else:
        print(obj.round(3).to_string(index=False))
        for key, val in obj.attrs.items():
            print(f"  [{key}] {val}")


def main() -> None:
    args = parse_args()
    workbook = Path(args.workbook).expanduser()
    if not workbook.is_absolute():
        workbook = BASE_DIR / workbook
    workbook = workbook.resolve()

    RESULTS.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    df, sources = load(workbook)
    audit_sources(df, sources)

    print("\nBuilding figures:")
    dist = q1_distribution(df)
    items, pillars = q2_framework(df)
    q3 = q3_characteristics(df)
    gaps = q4_score_gaps(df)
    alpha, itc = reliability(df)

    show("Q1  Overall level and distribution", dist)
    show("Q2  Pillars, weakest first (mean per item, max 2)", pillars)
    show("Q2  Items", items)
    show("Q3  Size", q3["size"])
    show("Q3  Exposure group totals", q3["exposure_totals"])
    show("Q3  Exposure group, mean score by item", q3["exposure_item_pattern"])
    show("Q3  Exposure group controlling for size (OLS)",
         add_ci(q3["exposure_controlling_size"], len(df)))
    show("Q3  Robustness: size as tertiles",
         add_ci(q3["exposure_robustness_tertiles"], len(df)))
    for key in [k for k in q3 if k.startswith("meta_")]:
        show(f"Q3  {key.replace('meta_', '')}", q3[key])
    show("Q4  Disclosure score gaps", gaps)
    print(f"\n{'=' * 74}\nReliability\n{'=' * 74}\nCronbach's alpha = {alpha:.3f}")
    print("Interpret cautiously: the eleven ordinal items cover multiple TCFD dimensions.")
    print(itc.round(3).to_string(index=False))

    dist.to_frame("value").to_csv(RESULTS / "q1_distribution.csv")
    items.to_csv(RESULTS / "q2_items.csv", index=False)
    pillars.to_csv(RESULTS / "q2_pillars.csv", index=False)
    for name, tbl in q3.items():
        tbl.to_csv(RESULTS / f"q3_{name}.csv", index=False)
    gaps.to_csv(RESULTS / "q4_score_gaps.csv", index=False)
    itc.to_csv(RESULTS / "reliability_item_total.csv", index=False)
    df[["ticker", "company", "gics_sector", "exposure", "index_weight_pct"]
       + ITEMS + PILLAR_ORDER + ["total"]].to_csv(RESULTS / "scores_merged.csv", index=False)

    workbook_hash = hashlib.sha256(workbook.read_bytes()).hexdigest()
    run_metadata = pd.Series({
        "workbook": workbook.name,
        "workbook_sha256": workbook_hash,
        "python_version": platform.python_version(),
        "pandas_version": pd.__version__,
        "numpy_version": np.__version__,
        "scipy_version": scipy.__version__,
        "matplotlib_version": matplotlib.__version__,
        "n_companies": len(df),
        "n_items": len(ITEMS),
        "n_source_records": len(sources),
    }, name="value")
    run_metadata.to_csv(RESULTS / "run_metadata.csv", header=True)
    print(f"\nTables written to {RESULTS}/")


if __name__ == "__main__":
    main()
