# Codebook

Scoring rules for the eleven TCFD recommended disclosures (TCFD, 2017).

**Version 2.0.** Revised after a first full pass over all fifty companies produced almost no variance. The revision log at the end records every change. Version 1.0 scores are kept as `data/scores_v1.csv`, not overwritten.

The rule I work under: criteria are fixed before coding starts and do not change mid-pass. If they turn out to be unworkable, I change them, log it, and rescore everything already done. That is what happened here.

## 1. The eleven items

The four TCFD pillars, and the eleven recommended disclosures beneath them.

Australian companies already report under this structure. AASB S2 follows IFRS S2, uses the same four pillars, and has legal force for Group 1 entities from annual periods starting on or after 1 January 2025 (AASB, 2024). Scoring against TCFD is scoring against what the law asks of them.

Pillar-level scoring would be too coarse. Fifty companies across four pillars gives too few possible totals to compare anything, and no way to check whether items meant to measure the same thing behave alike. Clarkson et al. (2008) built their index directly on the GRI guidelines on the same reasoning: an index anchored to a published framework measures better than one invented for the occasion.

## 2. The scale

| Score | Meaning |
|---|---|
| 0 | Nothing disclosed, or a cross-reference leading nowhere. |
| 1 | Disclosed in general terms. Says it does something without saying what, who, when, or how much. |
| 2 | Every element listed for that item is present. |

Ties go to the lower score. Consistent harshness is a bias I can name and discuss; inconsistency is not fixable.

**Why not binary.** A yes-or-no index counts topics addressed, not disclosure quality. Clarkson et al. (2008) separate "hard" items, which can be verified and which a poor performer cannot cheaply fake, from "soft" ones, which are unverifiable claims any company can make for free. Binary scoring gives both the same mark, so a company could tick all eleven boxes without saying anything checkable.

**Why specificity.** Wiseman (1982) scored environmental disclosures on whether companies gave numbers or only words. I use the same logic with one adjustment: several TCFD items ask about governance and internal process, which do not come with numbers. So the test is verifiability rather than quantification. Can the reader check it, argue with it, or compare it against another company.

**Why only three points.** More gradations mean more of my judgement in the data (Beattie et al., 2004). One coder, no second opinion: a coarse scale with clear edges beats a fine one with fuzzy edges.

**Elements are conjunctive.** This is the substantive change in version 2.0. Each item below lists the elements a disclosure must contain to score 2, and all of them must be present. Missing one gives a 1. Where an item lists disqualifiers, a disqualifying pattern caps the score at 1 regardless of what else appears.

Version 1.0 awarded a 2 for a named body or process plus *any one* supporting detail. Against the ASX 50 that separated nothing: three items scored 2 for all fifty companies, and thirty-eight of fifty sat within a point of the maximum.

The elements themselves are not mine. They are what the TCFD's guidance for all sectors asks organisations to provide for each recommended disclosure (TCFD, 2021a), with the topic guidance on risk management (TCFD, 2020a), scenario analysis (TCFD, 2020b), and metrics and targets (TCFD, 2021b). Taking them from the framework's own guidance is what keeps the tightened criteria from being a standard I invented after seeing the data.

## 3. Sample and reporting year

**Sample.** The fifty constituents of the SPDR S&P/ASX 50 ETF (SFY), from the fund's daily holdings file dated 14 August 2026, less cash and SPI 200 futures. Ticker, name, shares, weight and GICS classification carry into `companies.csv` unchanged. I use the fund's holdings export rather than an index page because it is a dated primary document anyone can download and check.

Index weight proxies company size. The index is float-adjusted market capitalisation weighted, so weight tracks float-adjusted rather than total market capitalisation, and companies with large founder or strategic stakes sit lower than their headline market capitalisation implies. WiseTech and Soul Patts are the clearest cases here.

Weights move daily with share prices, so the snapshot date is part of the method. It also sits about a year after the FY2025 reports for June balance dates. That mismatch touches the size variable only, but it is reason enough to treat the size association as indicative.

**Reporting year.** The most recent financial year ending on or before 31 December 2025, which puts 30 June, 30 September, 31 December, 31 March and 31 July balance dates all inside FY2025.

FY2025 is the most recent year with a report from all fifty. FY2026 is not. December balance dates had not reached year end when I sampled, and most June balance dates had not reported, though Commonwealth Bank had on 11 August 2026 and Telstra on 13 August 2026. Taking each company's latest report would have split the sample across two years by nothing more than position in the reporting calendar.

That split would not be random with respect to what I am measuring. AASB S2 applies to periods beginning on or after 1 January 2025, so December balance dates enter the mandatory regime a full year before June ones, and balance date correlates with industry because mining and energy report to December.

Fixing the year does not remove that problem, it relocates it. Inside FY2025, December balance dates are in the regime and June ones are not. I report that comparison descriptively where the metadata allows, but not as a finding: balance date, regime status and industry cannot be told apart at n = 50.

## 4. General rules

**Which document.** The amended Corporations Act 2001 (Cth) makes the sustainability report part of the annual report, so I read the annual report first, then any standalone sustainability, ESG or climate report if the climate content is absent or thin. Where both exist I read both, take the higher score, and record both in `sources.csv`. `report_location` records where the content sat.

**This period only.** Text repeated verbatim from last year counts. A pointer to last year's report that is not reproduced here does not.

**Length is not evidence.** Three paragraphs of general statements score what one paragraph of the same would (Beretta & Bozzolan, 2008).

**A framework index is not an element.** Many companies publish a TCFD content index mapping each disclosure to a page. The index never earns a score. I follow it to the page and score what is there. An index pointing at a general assertion scores 1.

**Elements must be in the disclosure.** If the risk committee is named on page 40 of the governance section but the climate section never connects it to climate, the element is not satisfied. I score what a reader of the climate disclosure learns.

**Evidence as I go.** Document, page and a one-line reason in `sources.csv` while scoring, not reconstructed afterwards. The note records which elements were present and which were missing, so anyone can see why a 1 is not a 2.

R_b and S_b depart from that format. Their notes were rewritten as prose quoting each company's specific content, which reads better but carries no parseable missing-element field, so those two items drop out of the element-level analysis. A separate structured column alongside the prose would restore them.

**Consolidation.** I score at group level where a company reports on a consolidated basis.

## 5. Governance

### G_a Board oversight

| Score | Criteria |
|---|---|
| 0 | Nothing about board or committee involvement in climate. |
| 1 | Board involvement described, one or more element missing. |
| 2 | All three elements. |

1. **Named body.** The specific board or committee holding climate responsibility, with climate in its stated remit.
2. **Frequency.** How often it considers climate: a meeting count, a stated cadence, a number of times in the period. Not "regularly" or "as required".
3. **Substance.** At least one climate matter the body reviewed, approved or decided this period. Approved the targets, endorsed the transition plan, reviewed scenario results, weighed climate in a named capital decision.

*Basis:* the guidance for all sectors asks for the processes and frequency by which the board is informed, whether it considers climate when reviewing strategy and budgets, and how it monitors progress against targets (TCFD, 2021a).

*Does not count:* climate listed among general ESG topics in a committee charter. A board skills matrix showing climate expertise, with nothing about what the board did with it.

### G_b Management's role

| Score | Criteria |
|---|---|
| 0 | Nothing about management responsibility for climate. |
| 1 | Responsibility described, one or more element missing. |
| 2 | All three elements. |

1. **Named role or committee.** A specific executive position or management committee. Not "management" or "the sustainability team".
2. **Reporting line.** How it reports to the board, or to which board committee.
3. **What it does.** How management is informed, or how it monitors. A list of responsibilities is not a process.

*Basis:* TCFD (2021a) asks whether climate responsibilities are assigned to management positions or committees, whether those report to the board, the organisational structure, and the processes by which management is informed and monitors.

*Does not count:* an organisation chart with no description. A named Chief Sustainability Officer with no reporting line and no described function.

## 6. Strategy

### S_a Risks and opportunities across horizons

| Score | Criteria |
|---|---|
| 0 | No specific risks or opportunities identified. |
| 1 | Identified, one or more element missing. |
| 2 | All four elements. |

1. **Horizons in years.** Short, medium and long term each given a period.
2. **Specific physical risks.** Named hazards, named assets, operations or regions. "Extreme weather" is not specific.
3. **Specific transition risks.** Named policy, legal, technology, market or reputational risks. "Regulatory change" is not specific.
4. **Opportunities, and risks mapped to horizons.** Which risks and opportunities fall in which horizon.

*Basis:* TCFD (2021a) asks organisations to say what they consider short, medium and long term to be, given asset lifetimes, and to describe the specific issues in each horizon that could have material financial impact. Element 4 is what makes the horizons do any work.

*Does not count:* a generic risk table with no time dimension. Considering climate "over the short, medium and long term" with no years attached, which scores 1.

### S_b Impact on business, strategy and financial planning

| Score | Criteria |
|---|---|
| 0 | No description of impact. |
| 1 | Impact described, one or more element missing. |
| 2 | All three elements. |

1. **Named business areas.** Products and services, supply chain, operations, adaptation and mitigation, research and development.
2. **Named financial planning dimension.** Operating costs, revenues, capital expenditure and allocation, acquisitions or divestments, asset values or useful lives, provisions, access to capital.
3. **A specific consequence.** A quantified figure, or a named decision taken or planned: a named capital programme, an asset written down, a divestment. Saying climate is factored into planning without naming what came out of it does not satisfy this.

*Basis:* TCFD (2021a) sets out both lists and asks how climate serves as an input to financial planning and affects financial position. Element 3 separates describing a process from disclosing its output. Version 1.0 made a dollar figure sufficient but not required, which let process description alone carry the item.

*Does not count:* a materiality matrix. Climate risks that "may affect" the business with no consequence named.

### S_c Strategic resilience under scenarios

| Score | Criteria |
|---|---|
| 0 | No scenario analysis done or mentioned. |
| 1 | Mentioned, one or more element missing. |
| 2 | All four elements. |

1. **Two scenarios, one at 1.5°C.** The Australian rules require at least two, one consistent with 1.5°C and one with higher warming (AASB, 2024).
2. **Named, with source.** NGFS, IEA, IPCC SSPs, or equivalent.
3. **Scope and horizon.** Which parts of the business, over what period.
4. **Differentiated findings.** Results that differ between scenarios. One conclusion of resilience, identical across scenarios, does not satisfy this.

*Basis:* the scenario analysis guidance treats inputs, assumptions, analytical choices and outputs as the substance of the disclosure, not the fact that an analysis happened (TCFD, 2020b).

Scenario analysis has transitional relief for the regime's first three years. Low scores here are a feature of the phase-in, and I say so when reporting results.

## 7. Risk Management

### R_a Identifying and assessing

| Score | Criteria |
|---|---|
| 0 | No process described. |
| 1 | Process described, one or more element missing. |
| 2 | All three elements. |

1. **Who and how often.** The function or body doing it, and the frequency.
2. **How significance is determined.** A likelihood and impact scale, a scoring method, a threshold, or a materiality definition applied to climate.
3. **Inputs.** Regulatory requirements, scenario outputs, asset-level hazard data, value chain information.

*Basis:* TCFD (2021a) asks how organisations determine the relative significance of climate risks against other risks, whether they consider existing and emerging regulation, and how they assess the size and scope of identified risks.

*Does not count:* climate risks identified "through the enterprise risk management process", with no account of what that process does.

### R_b Managing

| Score | Criteria |
|---|---|
| 0 | Nothing about managing or mitigating. |
| 1 | Management described, one or both elements missing. |
| 2 | Both elements. |

1. **Decision logic.** How the company chooses between mitigating, transferring, accepting and controlling a climate risk.
2. **A named risk linked to a named response.** One identified risk paired with the action taken against it this period. The disclosure has to make the connection; a list of initiatives elsewhere in the report does not.

*Basis:* TCFD (2021a) asks how organisations decide to mitigate, transfer, accept or control climate risks, and the risk management guidance treats the link between identified risks and responses as the point of the disclosure (TCFD, 2020a).

*Does not count:* a list of sustainability initiatives, emissions projects or community programmes not tied to an identified risk. This disqualifier matters most of any in the codebook. Every company in the sample publishes such a list, and under version 1.0 that list was enough for a 2, which is why this item had zero variance.

### R_c Integration

| Score | Criteria |
|---|---|
| 0 | No mention of integration. |
| 1 | Integration claimed, one or more element missing. |
| 2 | All three elements. |

1. **Named framework.** The enterprise risk framework, policy or register climate sits within.
2. **Shared machinery.** Same materiality thresholds, escalation paths or reporting channels as other risks, rather than a parallel process.
3. **Evidence in the period.** Climate appears as a named principal or material risk in the company's own risk disclosure.

*Basis:* TCFD (2021a) asks how climate risk processes are integrated into overall risk management; the risk management guidance is aimed at the difference between a parallel climate process and real integration (TCFD, 2020a). Element 3 is the check on that difference.

*Does not count:* a sentence saying climate risk is integrated into enterprise risk management, and nothing further.

## 8. Metrics and Targets

### M_a Metrics other than emissions

| Score | Criteria |
|---|---|
| 0 | No metrics beyond greenhouse gas emissions. |
| 1 | Non-emissions metrics given, one or more element missing. |
| 2 | All three elements. |

1. **Breadth.** Metrics from at least two of the seven cross-industry categories other than GHG emissions. The categories are in Appendix 2, Table A2.1 of the 2021 Annex, covering transition risk, physical risk, opportunities, capital deployment, internal carbon prices and remuneration alongside emissions (TCFD, 2021a; 2021b). I read Table A2.1 when classifying rather than working from memory.
2. **Definition or basis of preparation.** So the reader knows what was counted.
3. **Comparability.** A prior-year comparative or stated baseline for each metric.

*Basis:* the metrics guidance describes effective metrics as decision-useful, verifiable, consistent over time, and supported by narrative explaining how the data was prepared (TCFD, 2021b).

Emissions are scored under M_b and not counted twice here.

### M_b Scope 1, 2 and 3 emissions

| Score | Criteria |
|---|---|
| 0 | No figures, or Scope 1 only. |
| 1 | Figures given, one or more element missing. |
| 2 | All four elements. |

1. **Scope 1 and 2 with figures**, Scope 2 identified as location-based, market-based, or both.
2. **Scope 3 with figures, by GHG Protocol category.** A single undifferentiated total does not satisfy this.
3. **Basis of preparation.** Methodology, boundary or emission factor source, in the disclosure or a referenced document.
4. **Prior-year comparatives** for each scope reported.

*Basis:* the category breakdown and the location versus market split come from the GHG Protocol, which AASB S2 adopts as the measurement basis in place of the NGER methodology that had priority in the exposure draft (AASB, 2024). TCFD (2021b) asks for Scope 1 and 2 independent of materiality, encourages Scope 3, and asks for comparable historical periods.

Scope 3 has three years of transitional relief, so weak scores here are part of the transition.

External assurance is noted in `sources.csv` but does not affect this score. Assurance is not one of the eleven recommended disclosures and I did not want to smuggle an extra criterion into a framework-anchored index.

### M_c Targets and performance

| Score | Criteria |
|---|---|
| 0 | No emissions or climate targets. |
| 1 | Targets given, one or more element missing. |
| 2 | All four elements. |

1. **An interim target dated 2035 or earlier**, with a stated base year. A 2050 net zero aspiration alone does not satisfy this.
2. **Scope and type.** Which emissions scopes, and absolute or intensity-based.
3. **Quantified progress.** Performance against the interim target as a figure for this period. "On track" without a number does not satisfy this.
4. **Linked to a disclosed metric**, so progress can be traced.

*Basis:* reporting performance against targets, not just stating them, is part of the recommended disclosure (TCFD, 2017). TCFD (2021b) describes effective targets as linked to recorded metrics, quantified, and specified over time with baselines and interim targets displayed.

I record absolute versus intensity because an intensity target can be met while absolute emissions rise.

## 9. Climate exposure grouping

Used in analysis only. It played no part in scoring any company.

GICS sectors are not used directly: five of the eleven sectors here hold two companies each, and a mean from two companies moves entirely if either changes.

| Group | n | Definition |
|---|---|---|
| Transition | 16 | Revenue tied to emissions-intensive activity; exposed to carbon pricing, policy, technology substitution |
| Physical | 8 | Assets fixed in place, or supply chains exposed to weather |
| Indirect | 10 | Few own emissions; exposure through lending, underwriting, investment portfolios |
| Baseline | 16 | Residual: no concentrated climate exposure |

**Transition:** BHP, BSL, EVN, FMG, JHX, LYC, NEM, NST, PLS, RIO, S32, STO, WDS, ORG, APA, QAN.
**Physical:** GPT, SGP, GMG, SCG, TCL, COL, WOW, BXB.
**Indirect:** ANZ, CBA, NAB, WBC, ASX, MQG, SOL, IAG, QBE, SUN.
**Baseline:** TLS, CAR, WES, ALL, LNW, TLC, CSL, COH, RMD, SHL, SIG, MPL, ALQ, CPU, WTC, XRO.

The baseline group is a residual, not a benchmark and not a low-exposure sector. It holds software, biotechnology, medical devices, gaming, professional services, telecommunications and retail, and it is internally heterogeneous. Dummy coding requires one group to be omitted so the rest have something to be measured against; which one is omitted changes neither model fit nor predicted scores.

Four assignments are judgement calls, recorded so a reader can disagree with the decision rather than the whole grouping:

- **QAN to Transition.** Aviation is hard to abate and faces direct carbon pricing. It also carries physical exposure through airports and route disruption, so the other placement is defensible.
- **BXB, COL, WOW to Physical.** Timber supply for pallet pooling, cold chain and agricultural supply for the grocers. All three are less geographically fixed than a REIT, so this is the weaker end of the group.
- **SOL to Indirect.** GICS puts it in Financials and it is an investment holding company, though its holdings lean towards coal and resources.
- **MPL to Baseline.** Health insurance carries none of the property catastrophe exposure IAG, Suncorp and QBE underwrite.

Physical has eight members. Group means involving it are imprecise, and the coefficients move if two or three companies change groups. I say so wherever exposure results appear.

## 10. Calibration

Version 1.0 piloted on the first three companies, chosen from sectors with different climate exposure. Three was too few to reveal that the criteria did not discriminate; the ceiling effect only appeared once all fifty were coded and the distribution could be seen.

Version 2.0 calibrated against the observed range instead. I rescored the five highest and five lowest scorers under version 1.0 first. Had those ten failed to separate, the revision had failed and I would have come back to this file before rescoring the other forty.

They separated. Across all fifty, standard deviation rose from 2.41 to 4.07, companies at maximum fell from 23 to 4, and the range widened from 12–22 to 5–22. No company's score rose on any item under the stricter criteria, which is the check that the revision was applied as written.

## 11. What this cannot tell you

**Disclosure, not performance.** A company reporting carefully on a bad emissions trajectory scores well. Wiseman (1982) found environmental disclosures incomplete and unrelated to what companies were actually doing, and the literature since has not settled it (Clarkson et al., 2008).

**One coder.** Content analysis carries the coder's judgement (Beattie et al., 2004). Criteria were fixed before each pass and every score points to a document and page, so a reader can check any judgement. There is no inter-rater statistic.

**Criteria revised after seeing results.** The most serious limitation here, and I would rather state it than present version 2.0 as a single clean pass. Tightening a threshold after finding no variance risks fitting the instrument to a wanted result. Against that: the elements come from the framework's own guidance rather than being chosen to produce spread, nothing was rescored before this file was final, and version 1.0 scores are published alongside. A reader who thinks the revision unjustified can use `scores_v1.csv`.

**Equal weights.** All eleven items count the same. Weighting is possible but adds another layer of my judgement.

**One year.** A snapshot shows no trend.

## Revision log

| Date | Item | Change | Reason |
|---|---|---|---|
| 2026-08-18 | All eleven | A score of 2 changed from a named body or process plus any one supporting detail, to a set of elements all of which must be present. | Version 1.0 did not discriminate. G_a, G_b and R_b scored 2 for all fifty, giving three items zero variance; mean total was 20.56 of 22 with 38 of 50 at 21 or above. |
| 2026-08-18 | All eleven | Required elements sourced item by item to the TCFD guidance for all sectors and topic guidance. | To keep the tightened criteria framework-anchored rather than author-defined. |
| 2026-08-18 | G_a | Frequency and a named matter decided in the period both required, alongside the named body. | The guidance asks for body, frequency, and what the board considers. Version 1.0 accepted any one. |
| 2026-08-18 | G_b | Reporting line and a described process both required, alongside the named role. | Same reason. |
| 2026-08-18 | S_a | Physical and transition risks both specific, and risks mapped to the defined horizons. | Defining horizons and not applying them tells the reader nothing. |
| 2026-08-18 | S_b | A specific consequence, figure or named decision, now required. | Version 1.0 made quantification sufficient but not required, so process description alone carried the item. |
| 2026-08-18 | S_c | Scope and horizon of the analysis, and findings differing between scenarios. | An analysis whose result does not vary by scenario has not been usefully reported. |
| 2026-08-18 | R_a | Explicit criteria for determining significance now required. | The guidance asks how relative significance is determined. Version 1.0 accepted any of who, how often, or what goes in. |
| 2026-08-18 | R_b | Decision logic and an explicit risk-to-response pairing both required. Initiative lists not tied to an identified risk disqualified. | Zero variance under version 1.0, because a sustainability initiative list satisfied the item and every company publishes one. |
| 2026-08-18 | R_c | Climate must appear as a named principal or material risk in the period. | To separate real integration from a claim of it. |
| 2026-08-18 | M_a | Two of the seven cross-industry categories, with definitions and comparatives. | Version 1.0 needed only one non-emissions metric with a definition and a comparative, which a single energy metric met. |
| 2026-08-18 | M_b | Basis of preparation and prior-year comparatives added. | Consistency over time and a stated basis of preparation are part of effective disclosure in the metrics guidance. |
| 2026-08-18 | M_c | Quantified progress and linkage to a disclosed metric now required. | Version 1.0 asked for progress but not a number, which "on track" met. |
| 2026-08-23 | Documentation only | Added section 3 (sample source, snapshot date, reporting year rule) and section 9 (exposure grouping and its four judgement calls). Fixed section numbering, which skipped 6. | These decisions were made and applied but lived only in the analysis code and README. A codebook that does not record them cannot be audited. No criterion changed, nothing rescored. |
| 2026-08-23 | R_b, S_b | Recorded in section 4 that these two items' evidence notes are prose rather than the structured present/missing format. | The general rule said every note records present and missing elements. That stopped being true for these two after the notes were rewritten. |

## References

Australian Accounting Standards Board. (2024). *AASB S2 Climate-related disclosures*. AASB.

Beattie, V., McInnes, B., & Fearnley, S. (2004). A methodology for analysing and evaluating narratives in annual reports. *Accounting Forum, 28*(3), 205–236. https://doi.org/10.1016/j.accfor.2004.07.001

Beretta, S., & Bozzolan, S. (2008). Quality versus quantity: The case of forward-looking disclosure. *Journal of Accounting, Auditing & Finance, 23*(3), 333–376. https://doi.org/10.1177/0148558X0802300304

Clarkson, P. M., Li, Y., Richardson, G. D., & Vasvari, F. P. (2008). Revisiting the relation between environmental performance and environmental disclosure. *Accounting, Organizations and Society, 33*(4–5), 303–327. https://doi.org/10.1016/j.aos.2007.05.003

Task Force on Climate-related Financial Disclosures. (2017). *Recommendations of the Task Force on Climate-related Financial Disclosures*. Financial Stability Board.

Task Force on Climate-related Financial Disclosures. (2020a). *Guidance on risk management integration and disclosure*. Financial Stability Board.

Task Force on Climate-related Financial Disclosures. (2020b). *Guidance on scenario analysis for non-financial companies*. Financial Stability Board.

Task Force on Climate-related Financial Disclosures. (2021a). *Implementing the recommendations of the TCFD* (2021 annex). Financial Stability Board. https://assets.bbhub.io/company/sites/60/2021/07/2021-TCFD-Implementing_Guidance.pdf

Task Force on Climate-related Financial Disclosures. (2021b). *Guidance on metrics, targets, and transition plans*. Financial Stability Board.

Wiseman, J. (1982). An evaluation of environmental disclosures made in corporate annual reports. *Accounting, Organizations and Society, 7*(1), 53–63. https://doi.org/10.1016/0361-3682(82)90025-3
