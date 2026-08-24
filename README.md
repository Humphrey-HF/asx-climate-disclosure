# ASX 50 FY2025 Climate-Disclosure Quality Analysis

## Overview

This project evaluates the quality of FY2025 climate-related disclosures by 50 ASX 50 companies. Each company is assessed against the 11 recommended disclosures in the Task Force on Climate-related Financial Disclosures (TCFD) framework using a transparent 0–2 coding scheme.

The project is designed as a lightweight, auditable research workflow. The qualitative coding remains a human judgement guided by `codebook.md`, while the Python analysis, statistical tables and figures can be reproduced from the audited workbook.

## Research questions

1. **Q1 — Overall disclosure quality:** What is the level and distribution of total disclosure scores?
2. **Q2 — Framework coverage:** Is disclosure quality even across the 11 TCFD recommended disclosures and four pillars?
3. **Q3 — Company characteristics:** Is disclosure quality associated with company size or climate-exposure type?
4. **Q4 — Concentration of score gaps:** In which recommended disclosures are the largest aggregate score gaps found?

## Sample and reporting period

- **Sample:** 50 ASX 50 constituents identified from the included holdings data.
- **Reporting period:** FY2025.
- **Unit of analysis:** One company × one TCFD recommended disclosure.
- **Coding observations:** 50 companies × 11 items = 550 company-item assessments.
- **Source material:** FY2025 annual reports and, where available, standalone climate or sustainability disclosures.

The holdings source and processed company list are included in:

- `holdings-daily-au-en-sfy.xlsx`
- `companies_from_holdings.csv`

The report-source tracker is:

- `ASX50_FY2025_disclosure_sources.xlsx`

## Scoring method

Each of the 11 recommended disclosures is scored from 0 to 2:

- **0:** The disclosure does not satisfy the minimum codebook requirement.
- **1:** The disclosure is present but general, incomplete or insufficiently specific.
- **2:** The disclosure satisfies the item-specific requirements in the codebook.

The maximum company score is therefore:

```text
11 items × 2 points = 22 points
```

The complete item-level decision rules and exclusions are documented in `codebook.md`. The workbook `Sources` sheet records the score, document, page and company-specific evidence note for every one of the 550 coding decisions.

## Key findings

- The mean disclosure score was **16.40 out of 22**, equivalent to **74.5%** of the maximum available score.
- The median was **17.50**, the observed range was **5–22**, and four companies received the maximum score.
- Disclosure quality was moderately positively associated with company size (**Spearman ρ = 0.516, p < 0.001**).
- The size association remained evident when size was modelled as continuous log10 index weight and when companies were divided into size tertiles.
- After controlling for size, the Transition and Physical climate-exposure groups scored higher than the heterogeneous Reference group in both model specifications. Evidence for the Indirect group was less conclusive.
- The largest aggregate disclosure gaps occurred in **M_a, S_c, G_b and R_b**.
- Cronbach's alpha was **0.861**, indicating relatively high internal consistency, although the items are ordinal and cover multiple TCFD dimensions.

## Results

### Q1 — Overall level and distribution

The mean total score was 16.40 and the median was 17.50. The median exceeded the mean, and the distribution was negatively skewed, indicating that most companies were concentrated toward the higher end of the scale while a smaller group of low-scoring companies reduced the mean.

The Shapiro–Wilk test rejected normality (p = 0.007). Non-parametric statistics are therefore emphasised where appropriate.

### Q2 — Coverage across the TCFD framework

Mean item scores ranged from 1.14 to 1.68:

| Item | Mean score | Companies scoring 2 |
|---|---:|---:|
| M_c | 1.68 | 38 |
| R_c | 1.64 | 32 |
| G_a | 1.62 | 31 |
| S_b | 1.62 | 33 |
| R_a | 1.56 | 30 |
| S_a | 1.52 | 26 |
| M_b | 1.46 | 24 |
| G_b | 1.40 | 20 |
| R_b | 1.40 | 22 |
| S_c | 1.36 | 25 |
| M_a | 1.14 | 15 |

The Friedman test indicated that item-level scores were not evenly distributed across the framework (χ² = 51.5, p < 0.001). Metrics & Targets had the lowest mean pillar score, while Risk Management had the highest, although the differences between pillar means were modest.

### Q3 — Company size and climate exposure

Company size was the most consistent correlate of disclosure quality:

- Spearman correlation between index weight and total score: ρ = 0.516, p < 0.001.
- Pearson correlation between log10 index weight and total score: r = 0.470, p < 0.001.
- Continuous-size OLS coefficient: 4.299 total-score points per tenfold increase in index weight, p = 0.004.
- Size-tertile robustness check: large companies scored 3.395 points above small companies, p = 0.013.

The OLS coefficients are unstandardised and are expressed in total disclosure-score points out of 22. They are not correlation coefficients and are not restricted to the interval −1 to 1.

After controlling for company size in the continuous-size model:

| Climate-exposure group | Difference from Reference | p-value |
|---|---:|---:|
| Transition | +2.721 points | 0.035 |
| Physical | +3.338 points | 0.034 |
| Indirect | +2.001 points | 0.199 |

The size-tertile robustness model produced the same general pattern: the Transition and Physical coefficients remained positive with p < 0.05, while the Indirect coefficient remained less conclusive.

These climate-exposure categories are researcher-defined analytical groups and are not equivalent to GICS sectors. The project therefore does not establish that industry is unrelated to disclosure quality.

Additional descriptive comparisons show:

- Companies using standalone reports had a mean score of 16.67, compared with 16.00 for companies integrating disclosure into the annual report.
- The six companies classified as subject to AASB S2 had a mean score of 20.00, compared with 15.91 for the remaining companies. This small-group comparison does not isolate a regulatory effect.
- Domicile comparisons are not interpreted because almost all companies were Australian and the foreign-domicile groups were very small.

### Q4 — Concentration of disclosure score gaps

Q4 calculates score points lost relative to every company receiving the maximum score of 2 on each item. It does not attempt to parse standardised `Missing:` phrases from the natural-language evidence notes.

| Item | Mean score | Companies below 2 | Points lost |
|---|---:|---:|---:|
| M_a | 1.14 | 35 | 43 |
| S_c | 1.36 | 25 | 32 |
| G_b | 1.40 | 30 | 30 |
| R_b | 1.40 | 28 | 30 |
| M_b | 1.46 | 26 | 27 |
| S_a | 1.52 | 24 | 24 |
| R_a | 1.56 | 20 | 22 |
| G_a | 1.62 | 19 | 19 |
| S_b | 1.62 | 17 | 19 |
| R_c | 1.64 | 18 | 18 |
| M_c | 1.68 | 12 | 16 |

The largest gap occurred in M_a, followed by S_c. This indicates that the most common weaknesses concerned climate-related metrics and scenario analysis. G_b and R_b also represented substantial gaps, including management responsibility and explicit links between identified risks and management responses.

## Interpretation

Company size was the most stable correlate of climate-disclosure quality. Larger companies may have greater reporting capacity and may face stronger regulatory, investor and public scrutiny. However, the cross-sectional design does not establish that company size causes better disclosure.

Climate-exposure type also contained information beyond company size. Transition- and physical-risk-exposed companies recorded higher adjusted scores than the heterogeneous Reference group. Because the exposure categories are not equivalent to industry sectors, the analysis cannot determine whether GICS industry has an independent effect.

The findings also show that disclosure weaknesses were concentrated in particular parts of the TCFD framework rather than evenly distributed. Many companies mentioned climate change, but fewer provided sufficiently specific metrics, scenario analysis or explicit risk-response linkages to obtain the maximum score under the codebook.

## Conclusion

ASX 50 companies generally provided relatively mature FY2025 climate-related disclosures, but quality varied substantially across companies and recommended disclosure items.

Company size was the most consistent correlate of disclosure quality. The positive association was observed in bivariate correlation analysis and remained evident under two alternative regression specifications: continuous log10 index weight and size tertiles.

Climate-exposure type was also partially associated with disclosure quality. Transition- and physical-risk-exposed companies scored higher than the Reference group after controlling for size, whereas evidence for the Indirect group was less conclusive. The analysis does not directly test industry effects.

The most important remaining disclosure gaps concerned climate-related metrics, scenario analysis, management responsibility and explicit connections between identified risks and management responses. All findings are descriptive and exploratory and should not be interpreted as causal effects.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── analysis.py
├── codebook.md
├── asx50_coding_workbook_v2_2_auditable.xlsx
├── ASX50_FY2025_disclosure_sources.xlsx
├── holdings-daily-au-en-sfy.xlsx
├── companies_from_holdings.csv
├── results/
└── figures/
```

The local `ASX50_annual_report/` directory contains the underlying reports but is excluded from Git because the verified corpus is approximately 915 MB and consists largely of third-party copyrighted documents. The source tracker provides the report locations needed for audit and retrieval.

## Reproducing the analysis

Python 3.11 or later is recommended.

### 1. Create a virtual environment

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the analysis

```bash
python analysis.py
```

The default input is:

```text
asx50_coding_workbook_v2_2_auditable.xlsx
```

A different workbook can be supplied explicitly:

```bash
python analysis.py another_workbook.xlsx
```

The script validates that:

- exactly 50 companies are present;
- all item scores are 0, 1 or 2;
- all companies are assigned to an exposure group;
- all 550 company-item source records are present;
- the `Scores` and `Sources` sheets contain matching scores;
- every source record contains a document, page and evidence note.

It then writes reproducible CSV tables to `results/` and publication-ready PDF and PNG figures to `figures/`.

## Reproducibility boundary

The statistical analysis and figures are reproducible from the audited workbook. The original coding cannot be recreated deterministically by Python because the scores depend on document interpretation under the codebook.

Auditability is instead provided through three linked components:

1. `codebook.md` defines the scoring rules and exclusions.
2. The workbook `Sources` sheet records document-level and page-level evidence for every score.
3. `analysis.py` verifies the coding structure and reproduces all statistical outputs.

The strongest future extension would be a second independent coder and an inter-rater reliability statistic such as weighted Cohen's kappa.

## Limitations

- The analysis covers one reporting year and 50 companies.
- The design is cross-sectional and does not support causal inference.
- Index weight is a proxy for float-adjusted market capitalisation, not a complete measure of company size.
- Climate-exposure groups are researcher-defined and contain judgement.
- The Physical group contains only eight companies, limiting statistical power.
- GICS industry effects are not directly estimated because several sectors contain very small numbers of companies.
- Cronbach's alpha measures internal consistency, not coding validity or inter-rater agreement.
- The scores are based on public disclosure quality and do not measure companies' actual climate performance.
