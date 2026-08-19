# Codebook

How I score each of the eleven recommended disclosures in the TCFD framework (TCFD, 2017).

**Version 2.0. Revised after the first full pass over all fifty companies. See the revision log at the end for what changed and why. Scores produced under version 1.0 are retained in the repository as `scores_v1.csv` and are not overwritten.**

I wrote version 1.0 before scoring any company. Once coding starts I do not change the criteria. If a criterion turns out to be unworkable I change it, note the change in the revision log, and rescore every company already done. That is what has happened here, and every company is being rescored under version 2.0.

## 1. Why these eleven items

I score against the TCFD's four pillars and the eleven recommended disclosures beneath them (TCFD, 2017). Three reasons for choosing this over the GRI Standards or an index of my own.

It is the framework these companies actually report under. AASB S2 Climate-related Disclosures follows IFRS S2 and uses the same four pillars. Amendments to the Corporations Act 2001 (Cth) gave it legal force for Group 1 entities, for annual reporting periods starting on or after 1 January 2025 (AASB, 2024). So scoring Australian companies against TCFD means scoring them against the structure the law requires of them, not against something I imposed from outside.

The eleven items are what make the framework usable. The four pillars are written broadly so they work across every industry. The eleven disclosures beneath them say what a company actually has to tell you. If I scored only at pillar level, fifty companies would land on a handful of possible totals, which is too coarse to compare sectors, and I could not check whether items meant to measure the same thing behave consistently.

Building an index from a published framework is standard practice. Clarkson et al. (2008) built theirs directly on the GRI guidelines, arguing that an index anchored to a framework captures what you are trying to measure better than the ad hoc indices used before it.

## 2. Why a three-point scale

### 2.1 Why not simply present or absent

A yes-or-no index counts how much a company disclosed, not how good the disclosure was.

Clarkson et al. (2008) draw a useful line here. They separate "hard" disclosure items from "soft" ones. Hard items can be verified, and a poor performer cannot easily fake them. Soft items are unverifiable claims of commitment, and any company can make them at no cost. A binary index gives both the same score.

That matters for this project. Under a binary index a company could tick all eleven boxes, score full marks, and never say anything a reader could check. Compliance-style scoring tells you whether the required topics were addressed. It does not tell you whether what was said is accurate, balanced or complete.

### 2.2 Why grade by how specific the disclosure is

Wiseman (1982) did this first. Her environmental disclosure index scored each item on whether the company gave numbers or only words, and her approach is still the reference point for measuring environmental disclosure quality through content analysis.

I follow the same logic with one adjustment. Several TCFD items ask about governance arrangements and internal processes, which do not naturally come with numbers. So my test is whether the disclosure is verifiable, not whether it is quantified: does the reader get something they could check, argue with, or compare against another company.

### 2.3 Why not a finer scale

The more distinctions I ask myself to draw, the more of my own judgement ends up in the data, and the less reliable the measure becomes. Beattie et al. (2004) describe this trade-off between how rich a content analysis is and how objective it can be.

I am one coder with no second person checking my work. Under those conditions a coarse scale with clear edges beats a fine scale with fuzzy ones. Three points is the fewest that separates the three states I care about: nothing said, something asserted, something specific.

Version 2.0 keeps the three-point scale unchanged. What changed is the evidence required to reach each point, not the number of points.

### 2.4 The scale

| Score | Meaning |
|---|---|
| 0 | Nothing disclosed. The topic is absent, or the only reference is a cross-reference leading nowhere. |
| 1 | Disclosed in general terms. The company says it does something without saying what, who, when, or how much. A "soft" claim in the sense of Clarkson et al. (2008). |
| 2 | Disclosed specifically. Every element listed for that item is present, so a reader could check the disclosure or argue with it. |

If I cannot decide between two scores, I give the lower one. Scoring consistently harsh is a bias I can identify and discuss later. Scoring inconsistently is not fixable.

### 2.5 A 2 requires every element, not one of them

This is the substantive change in version 2.0.

In version 1.0 most items awarded a 2 when the company supplied a named body or process **and any one** of several supporting details. Applied to the ASX 50, that threshold did not separate anything. Three items scored 2 for all fifty companies, and thirty-eight of fifty companies sat within one point of the maximum. An instrument on which almost every case scores the same cannot support comparison between cases, which is what this project set out to do.

Under version 2.0, each item lists the elements a disclosure must contain to score 2. **All of them must be present.** Missing any one drops the score to 1. Where an item also lists disqualifiers, the presence of a disqualifying pattern caps the score at 1 regardless of what else is disclosed.

The elements are not mine. They are the content the TCFD's own guidance for all sectors asks organisations to provide for that recommended disclosure (TCFD, 2021a), supplemented by the TCFD's topic guidance on risk management integration (TCFD, 2020a), scenario analysis (TCFD, 2020b), and metrics, targets and transition plans (TCFD, 2021b). Anchoring the elements to the framework's own implementation guidance keeps the index framework-anchored in the sense Clarkson et al. (2008) argue for, and keeps me from inventing a standard of my own after seeing the data.

## 3. General rules

**Which document I read.** The amended Corporations Act 2001 (Cth) makes the sustainability report part of the annual report, so I read the annual report first. If the climate disclosure is not there, or is thin, I go to a standalone sustainability, ESG or TCFD report and record `report_location` as `standalone`. If both exist I read both, take the higher score, and record both documents in `sources.csv`.

**Only this reporting period counts.** Text repeated word for word from last year still counts. A pointer to last year's report that is not reproduced in this one does not.

**Length is not evidence.** Three paragraphs of general statements score the same as one paragraph saying the same thing. How much a company writes and how good the disclosure is are separate questions (Beretta & Bozzolan, 2008).

**A framework index is not an element.** Many companies publish a TCFD content index mapping each recommended disclosure to a page. The index itself never earns a score. I follow it to the page it points at and score what is written there. An index pointing to a page that contains only a general assertion scores 1.

**Elements must be in the disclosure, not inferred from elsewhere in the report.** If a company names its risk committee on page 40 of the governance section but the climate section never connects the committee to climate, the element is not satisfied. I am scoring what a reader of the climate disclosure learns.

**Every score gets evidence.** I record the document, the page, and a one-line reason in `sources.csv` as I score, not afterwards from memory. Under version 2.0 the note also records which required elements were present and which were missing, so a 1 can be distinguished from a 2 by anyone checking my work.

**I score at group level** where a company reports on a consolidated basis.

## 4. Governance

### G_a Board oversight of climate risks and opportunities

| Score | Criteria |
|---|---|
| 0 | Nothing about the board or a committee being involved in climate matters. |
| 1 | Some board involvement described, but one or more of the three elements below is missing. |
| 2 | All three elements present. |

Elements required for 2:

1. **Named body.** The specific board or board committee holding climate responsibility is named, and climate sits in its stated remit or terms of reference.
2. **Frequency.** How often the board or committee considers climate matters is stated, as a number of meetings, a stated cadence such as quarterly, or a count of times in the period. "Regularly" and "as required" do not satisfy this.
3. **Substance in the period.** At least one specific climate matter the body reviewed, approved or decided during the reporting period is named. Examples: approved the emissions targets, endorsed the transition plan, reviewed the scenario analysis results, considered climate in a named capital allocation decision.

Basis: the TCFD guidance for all sectors on this disclosure asks organisations to describe the processes and frequency by which the board is informed about climate-related issues, whether the board considers climate when reviewing strategy, major plans of action, risk management policies, budgets and business plans, and how the board monitors progress against climate goals and targets (TCFD, 2021a). The three elements are those three requests.

Does not count: listing climate among a general set of ESG or sustainability topics in a committee charter, with no climate-specific matter identified. Board skills matrices listing climate expertise, absent any description of what the board did with it.

### G_b Management's role in assessing and managing climate risks

| Score | Criteria |
|---|---|
| 0 | Nothing about management responsibility for climate matters. |
| 1 | Management responsibility described, but one or more of the three elements below is missing. |
| 2 | All three elements present. |

Elements required for 2:

1. **Named role or committee.** A specific executive position or management committee is named, not "management" or "the sustainability team".
2. **Reporting line.** How that role or committee reports to the board, or to which named board committee, is stated.
3. **What it does.** The process by which management is informed about climate matters, or how it monitors them, is described. A list of responsibilities is not a process.

Basis: the guidance for all sectors asks whether climate responsibilities have been assigned to management-level positions or committees, whether those positions report to the board, the associated organisational structure, and the processes by which management is informed about and monitors climate-related issues (TCFD, 2021a).

Does not count: an organisational chart with no accompanying description. Naming a Chief Sustainability Officer without saying to whom the role reports or what it does.

## 5. Strategy

### S_a Climate risks and opportunities over short, medium and long term

| Score | Criteria |
|---|---|
| 0 | No specific climate risks or opportunities identified. |
| 1 | Risks or opportunities identified, but one or more of the four elements below is missing. |
| 2 | All four elements present. |

Elements required for 2:

1. **Horizons defined in years.** Short, medium and long term are each given a period, such as to 2030, 2030 to 2040, beyond 2040.
2. **Specific physical risks.** Named hazards affecting named assets, operations or regions. "Extreme weather" alone is not specific.
3. **Specific transition risks.** Named policy, legal, technology, market or reputational risks. "Regulatory change" alone is not specific.
4. **Opportunities, and risks mapped to horizons.** Opportunities are identified, and the disclosure says which risks and opportunities fall in which time horizon.

Basis: the guidance asks organisations to describe what they consider short, medium and long term to be, taking into account the useful life of their assets and the time over which climate impacts typically manifest, and to describe the specific climate-related issues for each time horizon that could have a material financial impact (TCFD, 2021a). Element 4 is what makes the horizons do any work: defining them and then not using them leaves the reader no better informed.

Does not count: a generic risk table with no time dimension. Stating that the company considers climate risk over the short, medium and long term without attaching years, which scores 1.

### S_b Impact on business, strategy and financial planning

| Score | Criteria |
|---|---|
| 0 | No description of impact. |
| 1 | Impact described, but one or more of the three elements below is missing. |
| 2 | All three elements present. |

Elements required for 2:

1. **Named business areas.** Which parts of the business are affected, drawn from areas such as products and services, supply chain, operations, adaptation and mitigation activities, or research and development.
2. **Named financial planning dimension.** An explicit link to at least one of: operating costs, revenues, capital expenditure and capital allocation, acquisitions or divestments, asset values or useful lives, provisions, or access to capital.
3. **A specific consequence.** Either a quantified financial figure, or a named decision actually taken or planned, such as a named capital programme, a named asset written down or revalued, or a named divestment. A statement that climate is factored into planning, without naming what it produced, does not satisfy this.

Basis: the guidance sets out the business areas and the financial planning areas organisations should describe, and asks how climate-related issues serve as an input to financial planning, over what time periods, and how they affect financial performance and position (TCFD, 2021a). Element 3 is the difference between describing a process and disclosing its output. Version 1.0 treated a dollar figure as sufficient but not required, which in practice allowed the whole item to be satisfied by process description alone.

Does not count: a materiality matrix. A statement that climate risks "may affect" the business, with no consequence named.

### S_c Resilience of the strategy under different climate scenarios

| Score | Criteria |
|---|---|
| 0 | No scenario analysis done or mentioned. |
| 1 | Scenario analysis mentioned, but one or more of the four elements below is missing. |
| 2 | All four elements present. |

Elements required for 2:

1. **At least two scenarios, one of them 1.5°C.** Required by the Australian rules, which call for at least two scenarios, one consistent with 1.5°C and one with higher warming (AASB, 2024).
2. **Named scenarios with source.** Each scenario is named and its source given, such as the Network for Greening the Financial System, the International Energy Agency, or the IPCC Shared Socioeconomic Pathways.
3. **Scope and horizon of the analysis.** Which parts of the business were analysed, and over what time horizon.
4. **Differentiated findings.** What the analysis showed, with results that differ between scenarios. A single conclusion that the strategy is resilient, identical across scenarios, does not satisfy this.

Basis: the TCFD's scenario analysis guidance treats the disclosure of inputs, assumptions, analytical choices and outputs as the substance of the disclosure, not the fact that an analysis was performed (TCFD, 2020b). Element 4 follows: an analysis whose reported result does not vary by scenario has not been reported in a way a reader can use.

Scenario analysis attracts transitional relief in the first three years of the Australian regime. I read low scores here as a feature of the phase-in, not as a company failing, and I say so when reporting results.

### Risk Management

### R_a Processes for identifying and assessing climate risks

| Score | Criteria |
|---|---|
| 0 | No process described. |
| 1 | A process is described, but one or more of the three elements below is missing. |
| 2 | All three elements present. |

Elements required for 2:

1. **Who and how often.** The function or body that performs the identification and assessment, and the frequency of the exercise.
2. **How significance is determined.** The criteria used to decide that a climate risk is significant or material: a likelihood and impact scale, a scoring method, a threshold, or a stated materiality definition applied to climate.
3. **Inputs.** What feeds the assessment, such as existing and emerging regulatory requirements, scenario outputs, asset-level hazard data, or value chain information.

Basis: the guidance asks organisations to describe their risk identification and assessment processes including how they determine the relative significance of climate risks in relation to other risks, whether they consider existing and emerging regulatory requirements, and their processes for assessing the potential size and scope of identified risks (TCFD, 2021a).

Does not count: a statement that climate risks are identified through the enterprise risk management process, with no description of what that process does.

### R_b Processes for managing climate risks

| Score | Criteria |
|---|---|
| 0 | Nothing about managing or mitigating. |
| 1 | Management of risks described, but one or more of the two elements below is missing. |
| 2 | Both elements present. |

Elements required for 2:

1. **Decision logic.** How the company decides between mitigating, transferring, accepting and controlling a climate risk, or an equivalent stated framework for choosing a response.
2. **A named risk linked to a named response.** At least one specific identified climate risk is paired with the specific action taken in response to it during the period. The pairing must be explicit; a list of initiatives elsewhere in the report does not connect to the risk unless the disclosure connects them.

Basis: the guidance asks organisations to describe their processes for managing climate-related risks including how they make decisions to mitigate, transfer, accept or control those risks (TCFD, 2021a), and the risk management guidance treats the linkage between identified risks and responses as the point of the disclosure (TCFD, 2020a).

Does not count: a list of sustainability initiatives, emissions reduction projects or community programmes not tied to an identified risk. This is the disqualifier that matters most for this item, because such lists are near-universal and were sufficient to earn a 2 under version 1.0.

### R_c Integration into overall risk management

| Score | Criteria |
|---|---|
| 0 | No mention of integration. |
| 1 | Integration claimed, but one or more of the three elements below is missing. |
| 2 | All three elements present. |

Elements required for 2:

1. **Named framework.** The enterprise risk management framework, policy or risk register that climate sits within is named.
2. **Shared machinery.** The disclosure states that climate uses the same materiality thresholds, escalation paths or reporting channels as other risks, rather than a parallel process.
3. **Evidence in the period.** Climate appears as a named principal, material or top-tier risk in the company's own risk disclosure for the period, or an equivalent demonstration that integration operated rather than being described.

Basis: the guidance asks how the processes for identifying, assessing and managing climate risks are integrated into overall risk management (TCFD, 2021a), and the risk management guidance is directed at the difference between a parallel climate process and genuine integration (TCFD, 2020a). Element 3 is the check on that difference.

Does not count: a sentence stating that climate risk is integrated into enterprise risk management, with nothing further.

## 7. Metrics and Targets

### M_a Metrics used to assess climate risks and opportunities

| Score | Criteria |
|---|---|
| 0 | No metrics beyond greenhouse gas emissions. |
| 1 | Non-emissions metrics given, but one or more of the three elements below is missing. |
| 2 | All three elements present. |

Elements required for 2:

1. **Breadth.** Metrics covering at least two of the seven cross-industry metric categories other than GHG emissions. The seven categories are set out in Appendix 2, Table A2.1 of the 2021 Annex, and cover transition risk, physical risk, climate-related opportunities, capital deployment, internal carbon prices, and remuneration alongside emissions (TCFD, 2021a; TCFD, 2021b). I read Table A2.1 directly when classifying a metric rather than working from memory.
2. **Definition or basis of preparation.** Each metric is defined, or its basis of preparation stated, so the reader knows what was counted.
3. **Comparability.** A prior-year comparative or a stated baseline for each metric.

Basis: the metrics guidance describes effective metrics as decision-useful, clear and understandable, reliable, verifiable and objective, and consistent over time, and states that effective disclosure supports metrics with a corroborating narrative explaining the basis on which the data was prepared (TCFD, 2021b). Elements 2 and 3 are those characteristics made checkable.

I keep this separate from M_b on purpose. Emissions are scored under M_b and I do not count them twice here.

### M_b Scope 1, 2 and 3 greenhouse gas emissions

| Score | Criteria |
|---|---|
| 0 | No emissions figures, or Scope 1 only. |
| 1 | Emissions figures given, but one or more of the four elements below is missing. |
| 2 | All four elements present. |

Elements required for 2:

1. **Scope 1 and 2 with figures**, and Scope 2 identified as location-based, market-based, or both.
2. **Scope 3 with figures, broken down by GHG Protocol category.** A single undifferentiated Scope 3 total does not satisfy this.
3. **Basis of preparation.** The methodology, boundary or emission factor source is stated, whether in the disclosure or in a referenced basis of preparation document.
4. **Prior-year comparatives** for each scope reported.

Basis: the category breakdown and the location versus market-based split come from the GHG Protocol, which AASB S2 adopts as the measurement basis, replacing the NGER methodology that had priority in the exposure draft (AASB, 2024). The 2021 guidance asks all organisations to disclose Scope 1 and Scope 2 emissions independent of a materiality assessment, and encourages Scope 3 disclosure, with metrics reported for comparable historical periods (TCFD, 2021b).

Scope 3 also attracts transitional relief for three years, so I expect weak scores here and read them as part of the transition.

Whether the emissions are externally assured goes in `sources.csv` as a separate note and does not affect this score. Assurance is not one of the eleven recommended disclosures, and I did not want to smuggle an extra criterion into a framework-anchored index.

### M_c Targets and performance against them

| Score | Criteria |
|---|---|
| 0 | No emissions or climate targets. |
| 1 | Targets given, but one or more of the four elements below is missing. |
| 2 | All four elements present. |

Elements required for 2:

1. **An interim target dated 2035 or earlier**, with a stated base year. A 2050 net zero aspiration with no interim milestone does not satisfy this.
2. **Scope and type specified.** Which emissions scopes the target covers, and whether it is absolute or intensity-based.
3. **Quantified progress.** Performance against the interim target reported as a figure for the current period. "On track" without a number does not satisfy this.
4. **Linked to a disclosed metric.** The target is expressed in the same terms as a metric the company reports, so progress can be traced.

Basis: reporting performance against targets, not just stating them, is part of the recommended disclosure itself (TCFD, 2017). The metrics guidance describes effective targets as linked to metrics the organisation records, quantified and measurable, and clearly specified over time with time horizons, baselines and interim targets displayed (TCFD, 2021b). I record the absolute versus intensity split because an intensity target can be met while absolute emissions rise, so the two are not interchangeable.

## 8. Calibration

Version 1.0 used the first three companies as a pilot, chosen from sectors with different climate exposure. Three companies proved too few to reveal that the criteria did not discriminate. The ceiling effect only became visible once all fifty were coded and the distribution could be inspected.

For version 2.0 I calibrate against the observed range rather than the first three cases. I rescore the five companies that scored highest and the five that scored lowest under version 1.0 first. If those ten do not separate under the revised criteria, the revision has not worked and I return to this file before scoring the remaining forty.

## 9. What this instrument cannot tell you

**It measures disclosure, not performance.** A company that reports carefully on a bad emissions trajectory scores well here. Wiseman (1982) found corporate environmental disclosures were incomplete and unrelated to what companies were actually doing, and the literature since has not settled the question (Clarkson et al., 2008). Nothing in this index says anything about whether a company is decarbonising.

**One coder, no second opinion.** Content analysis carries the coder's judgement with it (Beattie et al., 2004). Three things limit the damage: the criteria were fixed before each pass, every score points to a document and page, and version 2.0 requires the `sources.csv` note to record which elements were present and which were missing, so a reader can reconstruct the judgement rather than take it on trust.

**The criteria were revised after seeing the results.** This is the most serious limitation of version 2.0 and I state it plainly rather than presenting the revised scores as though they came from a single clean pass. Tightening a threshold after observing that the original produced no variance risks fitting the instrument to a result I wanted. Three things constrain it: the revised elements are taken from the framework's own implementation guidance rather than chosen by me to produce spread, the version 1.0 scores are retained and reported alongside version 2.0 rather than replaced, and no company was rescored before this file was finalised. Readers who consider the revision unjustified can use `scores_v1.csv` and reach their own conclusion.

**Everything weighs the same.** All eleven items count equally towards the total. Weighting them is possible, but it would add another layer of my judgement, and leaving it out keeps the instrument easy to inspect.

**One year only.** A single snapshot shows no trend.

## Revision log

| Date | Item | Change | Reason |
|---|---|---|---|
| 2026-08-18 | All eleven | Criteria for a score of 2 changed from a named body or process plus any one supporting detail, to a named set of elements all of which must be present. | The version 1.0 criteria did not discriminate across the ASX 50. G_a, G_b and R_b scored 2 for all fifty companies, giving three items zero variance. The mean total was 20.56 of a possible 22, with 38 of 50 companies at 21 or above. An instrument on which almost every case scores the same cannot support comparison between cases. |
| 2026-08-18 | All eleven | Required elements sourced to the TCFD guidance for all sectors and the TCFD topic guidance, and cited item by item. | To keep the tightened criteria framework-anchored rather than author-defined, and to avoid a post-hoc standard invented to produce spread. |
| 2026-08-18 | G_a | Frequency and a named matter decided in the period both required, in addition to the named body. | The guidance for all sectors asks for the body, the frequency, and what the board considers and monitors. Version 1.0 accepted any one of these. |
| 2026-08-18 | G_b | Reporting line and a described process both required, in addition to the named role. | Same reason. |
| 2026-08-18 | S_a | Physical and transition risks must both be specific, and risks must be mapped to the defined horizons. | Defining horizons and then not applying them leaves the reader no better informed. |
| 2026-08-18 | S_b | A specific consequence, being a figure or a named decision, now required. | Version 1.0 treated quantification as sufficient but not required, which allowed the item to be satisfied by process description alone. |
| 2026-08-18 | S_c | Scope and horizon of the analysis, and findings that differ between scenarios, now required. | An analysis whose reported result does not vary by scenario has not been reported usefully. |
| 2026-08-18 | R_a | Explicit criteria for determining significance now required. | The guidance asks how the relative significance of climate risks is determined. Version 1.0 accepted any of who, how often, or what goes in. |
| 2026-08-18 | R_b | Decision logic and an explicit risk-to-response pairing both required. Lists of initiatives not tied to an identified risk now disqualified. | This item had zero variance under version 1.0 because a list of sustainability initiatives satisfied it, and every company in the sample publishes one. |
| 2026-08-18 | R_c | Evidence that climate appears as a named principal or material risk in the period now required. | To separate genuine integration from a claim of integration. |
| 2026-08-18 | M_a | Two of the seven cross-industry metric categories now required, with definitions and comparatives. | Version 1.0 required only non-emissions metrics with a definition and one comparative, which most companies met with a single energy metric. |
| 2026-08-18 | M_b | Basis of preparation and prior-year comparatives added to the existing scope requirements. | Consistency over time and a stated basis of preparation are characteristics the metrics guidance treats as part of effective disclosure. |
| 2026-08-18 | M_c | Quantified progress against the interim target, and linkage to a disclosed metric, now required. | Version 1.0 required progress to be reported but not quantified, which "on track" satisfied. |

## References

Australian Accounting Standards Board. (2024). *AASB S2 Climate-related disclosures*. AASB.

Beattie, V., McInnes, B., & Fearnley, S. (2004). A methodology for analysing and evaluating narratives in annual reports: A comprehensive descriptive profile and metrics for disclosure quality attributes. *Accounting Forum, 28*(3), 205–236. https://doi.org/10.1016/j.accfor.2004.07.001

Beretta, S., & Bozzolan, S. (2008). Quality versus quantity: The case of forward-looking disclosure. *Journal of Accounting, Auditing & Finance, 23*(3), 333–376. https://doi.org/10.1177/0148558X0802300304

Clarkson, P. M., Li, Y., Richardson, G. D., & Vasvari, F. P. (2008). Revisiting the relation between environmental performance and environmental disclosure: An empirical analysis. *Accounting, Organizations and Society, 33*(4–5), 303–327. https://doi.org/10.1016/j.aos.2007.05.003

Task Force on Climate-related Financial Disclosures. (2017). *Recommendations of the Task Force on Climate-related Financial Disclosures*. Financial Stability Board.

Task Force on Climate-related Financial Disclosures. (2020a). *Guidance on risk management integration and disclosure*. Financial Stability Board.

Task Force on Climate-related Financial Disclosures. (2020b). *Guidance on scenario analysis for non-financial companies*. Financial Stability Board.

Task Force on Climate-related Financial Disclosures. (2021a). *Implementing the recommendations of the Task Force on Climate-related Financial Disclosures* (2021 annex). Financial Stability Board. https://assets.bbhub.io/company/sites/60/2021/07/2021-TCFD-Implementing_Guidance.pdf

Task Force on Climate-related Financial Disclosures. (2021b). *Guidance on metrics, targets, and transition plans*. Financial Stability Board.

Wiseman, J. (1982). An evaluation of environmental disclosures made in corporate annual reports. *Accounting, Organizations and Society, 7*(1), 53–63. https://doi.org/10.1016/0361-3682(82)90025-3
