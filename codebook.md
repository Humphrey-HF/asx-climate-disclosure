# Codebook

How I score each of the eleven recommended disclosures in the TCFD framework (TCFD, 2017).

I wrote this before scoring any company. Once coding starts I do not change it. If a criterion
turns out to be unworkable during the pilot, I change it, note the change in the revision log at
the end of this file, and rescore every company I have already done.


## 1. Why these eleven items

I score against the TCFD's four pillars and the eleven recommended disclosures beneath them
(TCFD, 2017). Three reasons for choosing this over the GRI Standards or an index of my own.

**It is the framework these companies actually report under.** AASB S2 *Climate-related
Disclosures* follows IFRS S2 and uses the same four pillars. Amendments to the *Corporations Act
2001* (Cth) gave it legal force for Group 1 entities, for annual reporting periods starting on
or after 1 January 2025 (AASB, 2024). So scoring Australian companies against TCFD means scoring
them against the structure the law requires of them, not against something I imposed from
outside.

**The eleven items are what make the framework usable.** The four pillars are written broadly so
they work across every industry. The eleven disclosures beneath them say what a company actually
has to tell you. If I scored only at pillar level, fifty companies would land on a handful of
possible totals, which is too coarse to compare sectors, and I could not check whether items
meant to measure the same thing behave consistently.

**Building an index from a published framework is standard practice.** Clarkson et al. (2008)
built theirs directly on the GRI guidelines, arguing that an index anchored to a framework
captures what you are trying to measure better than the ad hoc indices used before it.

---

## 2. Why a three-point scale

### 2.1 Why not simply present or absent

A yes-or-no index counts how much a company disclosed, not how good the disclosure was.

Clarkson et al. (2008) draw a useful line here. They separate "hard" disclosure items from
"soft" ones. Hard items can be verified, and a poor performer cannot easily fake them. Soft
items are unverifiable claims of commitment, and any company can make them at no cost. A binary
index gives both the same score.

That matters for this project. Under a binary index a company could tick all eleven boxes, score
full marks, and never say anything a reader could check. Compliance-style scoring tells you
whether the required topics were addressed. It does not tell you whether what was said is
accurate, balanced or complete.

### 2.2 Why grade by how specific the disclosure is

Wiseman (1982) did this first. Her environmental disclosure index scored each item on whether
the company gave numbers or only words, and her approach is still the reference point for
measuring environmental disclosure quality through content analysis.

I follow the same logic with one adjustment. Several TCFD items ask about governance
arrangements and internal processes, which do not naturally come with numbers. So my test is
whether the disclosure is **verifiable**, not whether it is quantified: does the reader get
something they could check, argue with, or compare against another company.

### 2.3 Why not a finer scale

The more distinctions I ask myself to draw, the more of my own judgement ends up in the data,
and the less reliable the measure becomes. Beattie et al. (2004) describe this trade-off between
how rich a content analysis is and how objective it can be.

I am one coder with no second person checking my work. Under those conditions a coarse scale
with clear edges beats a fine scale with fuzzy ones. Three points is the fewest that separates
the three states I care about: nothing said, something asserted, something specific.

### 2.4 The scale

| Score | Meaning |
|---|---|
| **0** | Nothing disclosed. The topic is absent, or the only reference is a cross-reference leading nowhere. |
| **1** | Disclosed in general terms. The company says it does something without saying what, who, when, or how much. A "soft" claim in the sense of Clarkson et al. (2008). |
| **2** | Disclosed specifically. Names a body, defines a period, gives a figure, or describes a process, so a reader could check it or argue with it. |

**If I cannot decide between two scores, I give the lower one.** Scoring consistently harsh is a
bias I can identify and discuss later. Scoring inconsistently is not fixable.

---

## 3. General rules

**Which document I read.** The amended *Corporations Act 2001* (Cth) makes the sustainability
report part of the annual report, so I read the annual report first. If the climate disclosure
is not there, or is thin, I go to a standalone sustainability, ESG or TCFD report and record
`report_location` as `standalone`. If both exist I read both, take the higher score, and record
both documents in `sources.csv`.

**Only this reporting period counts.** Text repeated word for word from last year still counts.
A pointer to last year's report that is not reproduced in this one does not.

**Length is not evidence.** Three paragraphs of general statements score the same as one
paragraph saying the same thing. How much a company writes and how good the disclosure is are
separate questions (Beretta & Bozzolan, 2008).

**Every score gets evidence.** I record the document, the page, and a one-line reason in
`sources.csv` as I score, not afterwards from memory.

**I score at group level** where a company reports on a consolidated basis.

---

## 4. Governance

### G_a Board oversight of climate risks and opportunities

| Score | Criteria |
|---|---|
| 0 | Nothing about the board or a committee being involved in climate matters. |
| 1 | Says the board oversees climate risk, but does not say which body, how often, or what it decides. |
| 2 | Names the responsible board or committee **and** gives either how often climate comes up or what specifically it reviews or approves, such as targets, the transition plan, or scenario analysis results. |

Handing the job to a named committee counts. The difference between 1 and 2 is whether the
reader learns which body, how often, or on what. These are the elements the supplemental
guidance for this disclosure asks for (TCFD, 2017).

### G_b Management's role in assessing and managing climate risks

| Score | Criteria |
|---|---|
| 0 | Nothing about management responsibility for climate matters. |
| 1 | Says management is responsible, without naming a role, position or committee. |
| 2 | Names the executive role or management committee **and** describes either how it reports to the board or what it actually does. |

---

## 5. Strategy

### S_a Climate risks and opportunities over short, medium and long term

| Score | Criteria |
|---|---|
| 0 | No specific climate risks or opportunities identified. |
| 1 | Identifies risks in general terms, **or** leaves out opportunities, **or** mentions time horizons without saying what they are. |
| 2 | Identifies specific physical **and** transition risks, identifies opportunities, **and** says what short, medium and long term mean in years. |

The disclosure itself asks companies to define the horizons, not just refer to them (TCFD,
2017). "We consider climate risk over the short, medium and long term", with no years attached,
is an assertion and scores 1.

### S_b Impact on business, strategy and financial planning

| Score | Criteria |
|---|---|
| 0 | No description of impact. |
| 1 | Says climate matters affect the business, with no link to financial planning or where money goes. |
| 2 | Describes impacts on named parts of the business **and** connects them to financial planning: capital spending, asset values, provisions, research and development, or portfolio decisions. Putting a dollar figure on it is enough but not required. |

### S_c Resilience of the strategy under different climate scenarios

| Score | Criteria |
|---|---|
| 0 | No scenario analysis done or mentioned. |
| 1 | Mentions scenario analysis but uses only one scenario, **or** does not say which scenarios, **or** reports no result from it. |
| 2 | Uses at least two scenarios including a 1.5°C one, names them or their source, **and** says what the analysis showed about how resilient the strategy is. |

The two-scenario line is not my judgement call. The Australian rules require at least two
scenarios, one of them 1.5°C and one with higher warming (AASB, 2024). Scenarios companies
commonly cite come from the Network for Greening the Financial System, the International Energy
Agency, or the IPCC Shared Socioeconomic Pathways.

Scenario analysis gets transitional relief in the first three years of the regime. I read low
scores here as a feature of the phase-in, not as a company failing.

---

## 6. Risk Management

### R_a Processes for identifying and assessing climate risks

| Score | Criteria |
|---|---|
| 0 | No process described. |
| 1 | Says climate risks are identified and assessed, without saying how. |
| 2 | Describes the process: who does it, how often, what goes into it, or how they decide a risk is significant. |

### R_b Processes for managing climate risks

| Score | Criteria |
|---|---|
| 0 | Nothing about managing or mitigating. |
| 1 | Says identified risks are managed, without describing actions or how decisions are made. |
| 2 | Describes specific actions taken in response to identified risks, **or** how the company chooses between accepting, transferring, reducing and controlling a climate risk. |

### R_c Integration into overall risk management

| Score | Criteria |
|---|---|
| 0 | No mention of integration. |
| 1 | Claims climate risk is integrated into enterprise risk management, without explaining how. |
| 2 | Explains the integration: climate sits in a named risk framework or risk register, uses the same materiality or escalation thresholds as other risks, or reports through the same channels. |

---

## 7. Metrics and Targets

### M_a Metrics used to assess climate risks and opportunities

| Score | Criteria |
|---|---|
| 0 | No metrics beyond greenhouse gas emissions. |
| 1 | Lists non-emissions metrics with no definition, baseline or prior-year figure. |
| 2 | Gives non-emissions metrics with definitions and either a prior-year comparison or a stated baseline. Examples: capital put into climate solutions, exposure to carbon-intensive assets or sectors, an internal carbon price, energy intensity, or water use where it is climate-linked. |

I keep this separate from M_b on purpose. Emissions are scored under M_b and I do not count them
twice here.

### M_b Scope 1, 2 and 3 greenhouse gas emissions

| Score | Criteria |
|---|---|
| 0 | No emissions figures, or Scope 1 only. |
| 1 | Scope 1 and 2 given with figures, but Scope 3 is missing, mentioned without numbers, or given as one lump total. |
| 2 | Scope 1, 2 and 3 all given with figures, **and** Scope 3 broken down by category, **and** Scope 2 identified as location-based, market-based, or both. |

The category breakdown and the location-versus-market split come from the GHG Protocol, which
AASB S2 adopts as the measurement basis, replacing the NGER methodology that had priority in the
exposure draft (AASB, 2024).

Scope 3 also gets transitional relief for three years, so I expect weak scores here and read
them as part of the transition.

Whether the emissions are externally assured goes in `sources.csv` as a separate note and does
not affect this score. Assurance is not one of the eleven recommended disclosures, and I did not
want to smuggle an extra criterion into a framework-anchored index.

### M_c Targets and performance against them

| Score | Criteria |
|---|---|
| 0 | No emissions or climate targets. |
| 1 | Gives a distant aspiration such as net zero by 2050 with no interim milestone, **or** gives targets with no base year, **or** does not report how it is tracking against them. |
| 2 | Gives an interim target dated 2035 or earlier with a stated base year, says which scopes it covers, says whether it is absolute or intensity-based, **and** reports progress against it. |

Reporting performance against targets, not just stating them, is part of the disclosure itself
(TCFD, 2017). I record the absolute-versus-intensity split because an intensity target can be
met while absolute emissions rise, so the two are not interchangeable.

---

## 8. Pilot

The first three companies are a pilot. I choose them from sectors with very different climate
exposure so the criteria get tested at their edges. Anything ambiguous gets fixed here, logged
below, and the three pilot companies get rescored before I go on.

---

## 9. What this instrument cannot tell you

**It measures disclosure, not performance.** A company that reports carefully on a bad emissions
trajectory scores well here. Wiseman (1982) found corporate environmental disclosures were
incomplete and unrelated to what companies were actually doing, and the literature since has not
settled the question (Clarkson et al., 2008). Nothing in this index says anything about whether
a company is decarbonising.

**One coder, no second opinion.** Content analysis carries the coder's judgement with it
(Beattie et al., 2004). Two things limit the damage: I fixed the codebook before I started, and
every score points to a document and page, so anyone can check a judgement they disagree with.

**Everything weighs the same.** All eleven items count equally towards the total. Weighting them
is possible, but it would add another layer of my judgement, and leaving it out keeps the
instrument easy to inspect.

**One year only.** A single snapshot shows no trend.

---

## Revision log

Any change I make to the criteria after scoring has begun goes here. If this table is empty, the
same criteria were applied to all fifty companies.

| Date | Item | Change | Reason |
|---|---|---|---|
| | | | |

---

## References

Australian Accounting Standards Board. (2024). *AASB S2 Climate-related disclosures*. AASB.

Beattie, V., McInnes, B., & Fearnley, S. (2004). A methodology for analysing and evaluating
narratives in annual reports: A comprehensive descriptive profile and metrics for disclosure
quality attributes. *Accounting Forum, 28*(3), 205–236.
https://doi.org/10.1016/j.accfor.2004.07.001

Beretta, S., & Bozzolan, S. (2008). Quality versus quantity: The case of forward-looking
disclosure. *Journal of Accounting, Auditing & Finance, 23*(3), 333–376.
https://doi.org/10.1177/0148558X0802300304

Clarkson, P. M., Li, Y., Richardson, G. D., & Vasvari, F. P. (2008). Revisiting the relation
between environmental performance and environmental disclosure: An empirical analysis.
*Accounting, Organizations and Society, 33*(4–5), 303–327.
https://doi.org/10.1016/j.aos.2007.05.003

Task Force on Climate-related Financial Disclosures. (2017). *Recommendations of the Task Force
on Climate-related Financial Disclosures*. Financial Stability Board.

Wiseman, J. (1982). An evaluation of environmental disclosures made in corporate annual reports.
*Accounting, Organizations and Society, 7*(1), 53–63.
https://doi.org/10.1016/0361-3682(82)90025-3
