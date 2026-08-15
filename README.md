# asx-climate-disclosure
# ASX 50 Climate Disclosure Quality

# Scoring the quality of climate-related disclosures across the S&P/ASX 50 against the four pillars of the TCFD framework, in the first year of Australia's mandatory climate reporting regime.

# Status: in progress. Coding is under way. Findings will be added here once scoring is complete.

# Why this, and why now

# Australia's climate reporting moved from voluntary to mandatory in 2025. AASB S2 Climate-related Disclosures, modelled on IFRS S2 and built around the four TCFD pillars, was given legal force through amendments to the Corporations Act 2001, and applies to Group 1 entities for annual reporting periods beginning on or after 1 January 2025.Because Australian companies have different financial year ends, they enter the regime at different times. A company with a 31 December balance date has already published under AASB S2; one with a 30 June balance date is publishing its first mandatory report now; one with a 30 September balance date has not yet reached the end of its first mandatory period. The result is a transitional year in which mandatory and voluntary disclosure sit side by side across a single index.That makes this a useful moment to ask a simple question: how good is the disclosure actually is, and where is it weakest?

# Framework

# Disclosure is scored against the eleven recommended disclosures of the TCFD framework, grouped under its four pillars.TCFD was chosen over alternatives such as GRI or SASB for three reasons. It is the structure AASB S2 is built on, so for Australian entities it is the operative regulatory architecture rather than an arbitrary lens. It has been carried into IFRS S1 and S2 following the TCFD's own dissolution in 2023, making it the current global baseline. And it has precedent in the academic literature as a scoring frame for disclosure indices.The pillars are deliberately broad; the eleven recommended disclosures beneath them are what make the framework operable. Scoring at the pillar level alone would compress fifty companies into too few distinct values to support comparison, and would make internal consistency checks impossible.

# Item	Pillar	Recommended disclosure
G_a	Governance	Board oversight of climate-related risks and opportunities
G_b	Governance	Management's role in assessing and managing climate-related risks
S_a	Strategy	Climate risks and opportunities identified over short, medium and long term
S_b	Strategy	Impact on business, strategy and financial planning
S_c	Strategy	Resilience of strategy under different climate scenarios
R_a	Risk Management	Processes for identifying and assessing climate-related risks
R_b	Risk Management	Processes for managing climate-related risks
R_c	Risk Management	Integration into overall risk management
M_a	Metrics and Targets	Metrics used to assess climate-related risks and opportunities
M_b	Metrics and Targets	Scope 1, 2 and 3 greenhouse gas emissions
M_c	Metrics and Targets	Targets and performance against them

# Each item is scored on a three-point ordinal scale, for a maximum of 22.

# Score	Meaning
0	Not disclosed
1	Narrative or generic mention only, without specifics
2	Specific and verifiable content
A binary present/absent scale would measure compliance rather than quality: a company can address every recommended disclosure while saying nothing substantive about any of them. The three-point scale is intended to separate those cases. Full criteria for each item, written before scoring began, are in codebook.md.

# Sample

# Constituents of the S&P/ASX 50 as at 14 August 2026, taken from the daily holdings disclosure of the State Street SPDR S&P/ASX 50 ETF (ASX: SFY), the only ETF replicating the index. Cash and SPI 200 index futures were excluded as fund cash management rather than index constituents, leaving n = 50.

# The index is compiled by S&P Dow Jones Indices and reviewed quarterly, so membership is point-in-time: roughly a fifth of constituents changed over the twelve months to August 2026. The source file is archived in data/raw/ so the sample can be reconstructed exactly, independent of whether the original remains available.

# Four constituents are incorporated outside Australia and may fall outside the AASB S2 regime. These are flagged in companies.csv and treated as a separate group in the analysis rather than dropped.

# Repository structure
├── codebook.md                     Scoring criteria for each of the eleven items
├── data/
│   ├── raw/                        Archived source files, unmodified
│   ├── companies.csv               Sample frame
│   ├── scores.csv                  One row per company, one column per item
│   └── sources.csv                 Document and page evidence for every score
├── analysis/                       Analysis scripts
└── figures/                        Generated charts

# asx50_coding_workbook.xlsx is the working file used for manual entry; the CSV files exported from it are the inputs to the analysis and the version-controlled record.

# Method
Locate the most recent annual report for each constituent. Under AASB S2 the sustainability report is a component of the annual report, so the annual report is checked first; where climate disclosure is absent there, a standalone sustainability report is used and the location recorded.
Score each of the eleven items against the codebook.
Record the document and page supporting every score in sources.csv at the time of scoring.
Analyse by pillar, by GICS sector, by mandatory versus voluntary status, and against index weight.
Limitations

This measures disclosure, not performance. A company that reports thoroughly on a poor emissions trajectory scores well here. The index says nothing about whether a company is actually decarbonising.
Single coder, no inter-rater reliability check. Content analysis of this kind is exposed to coder judgement. Two mitigations are in place: the codebook was fixed before scoring began, and every score carries a document and page reference, so any individual judgement can be audited and disputed.
One reporting period. No trend can be observed from a single cross-section.Scope 3 and scenario analysis carry transitional relief. AASB S2 provides limited exemptions for Scope 3 emissions, scenario analysis and transition plans in the first three years. Weak scores on those items reflect the transitional arrangements as much as reporting capability, and are interpreted accordingly rather than read as failure.

# Sources
AASB S2 Climate-related Disclosures, Australian Accounting Standards Board
TCFD, Recommendations of the Task Force on Climate-related Financial Disclosures (2017)
S&P Dow Jones Indices, S&P/ASX 50 index methodology
State Street Global Advisors, SPDR S&P/ASX 50 ETF daily holdings, 14 August 2026
# Licence：MIT
