---
id: 04-work-plan
type: work-plan
step: 4
title: "Work Plan"
status: draft
addresses: "01-problem-definition.md#kq"
plans_for:
  - "03-priority-matrix.md#fa-city"
  - "03-priority-matrix.md#fa-competition"
  - "03-priority-matrix.md#fa-subsidy"
workstreams:
  - anchor: "04-work-plan.md#ws-a"
    label: "WS-A: City Portfolio Decisions"
    focus_area: "03-priority-matrix.md#fa-city"
  - anchor: "04-work-plan.md#ws-b"
    label: "WS-B: Competitive Constraint Boundaries"
    focus_area: "03-priority-matrix.md#fa-competition"
  - anchor: "04-work-plan.md#ws-c"
    label: "WS-C: Subsidy Precision Opportunity"
    focus_area: "03-priority-matrix.md#fa-subsidy"
---

# Step 4: Work Plan

## Workstream Overview

| Workstream | Focus Area | # Analyses | Effort | Key Dependency |
|------------|-----------|-------------|--------|---------------|
| **WS-A: City Portfolio Decisions** | City selection & resource allocation | 5 | 40% | None — data ready |
| **WS-B: Competitive Constraint Boundaries** | Competition ceiling | 3 | 30% | Web research (subagent) |
| **WS-C: Subsidy Precision Opportunity** | User quality improvement | 3 | 30% | WS-B scenarios feed into C3 |

**Total analyses: 11** | **Deadline: End of May 3** | **Review gate: May 4**

---

## Critical Path

```
WS-A (parallel analyses) ──────────────────→ AX-A4 EBIT Scenario ──────────────────┐
                                                                                   │
WS-B: Research ─→ AX-B1+B2 ─→ AX-B3 Competitive Scenarios ─────────────────────┼──▶ Step 5 Findings
                                                                                   │
WS-C: AX-C1 ─→ AX-C2 ─→ AX-C3 Subsidy Scenarios (feeds on WS-B output) ─────────┘
```

**Gating rule**: AX-A4 (EBIT scenario model) gates the final recommendation. AX-B3 gates AX-C3 (subsidy reallocation scenarios need competitive ceiling inputs).

---

## WS-A: City Portfolio Decisions

### AX-A1: 10-City Comparative Financial Analysis
- **Question**: Which cities have the best/worst unit economics and why?
- **Approach**: Cross-sectional comparison of all 10 cities on AOV, fulfillment cost, subsidy, cost/AOV, high-value user %, large supermarket %, category mix
- **Data**: 10-city dataset in 01-problem-definition.md
- **Data Status**: ✅ Available
- **Output**: City ranking table + 2×2 matrix (AOV × Cost/AOV)
- **Hypothesis**: C3/C7/C8 are best-in-class on different dimensions; C9/C10/C4 are structurally disadvantaged
- **Priority**: P1
- **Dependencies**: None

### AX-A2: Three Hemorrhage-Cities Profit Path Analysis
- **Question**: How does each of the 3 priority cities (Quanzhou/Huizhou/Weihai) achieve EBIT+? Are the paths different?
- **Approach**: Unit economics decomposition per city; identify primary EBIT driver
- **Data**: 01-problem-definition.md (city-level metrics)
- **Data Status**: ✅ Available
- **Output**: 3-city comparison table; EBIT driver attribution
- **Hypothesis**: Quanzhou wins via large supermarket depth; Huizhou via scale; Weihai via high AOV. Three different paths = "replicable model" requires three playbooks
- **Priority**: P1
- **Dependencies**: AX-A1 (can run in parallel)

### AX-A3: Selective Contraction Cost-Benefit Analysis
- **Question**: What fixed cost savings and subsidy reduction would result from exiting or shrinking C9/C10/C4/C5?
- **Approach**: Estimate annual loss per city; model savings from exiting (fixed cost allocation relief + subsidy elimination); sensitivity on partial vs. full exit
- **Data**: 01-problem-definition.md (annual loss estimates)
- **Data Status**: ✅ Available (but loss figures are estimated, not actual)
- **Output**: Savings range table (partial / full exit); recommended exit sequencing
- **Hypothesis**: Full exit from 2 worst cities saves ~3,000万 annually; partial exit of 4 evaluation cities saves ~2,000万
- **Priority**: P1
- **Dependencies**: AX-A1 (can run in parallel)

### AX-A4: 3+3+4 City Grouping EBIT Scenario Model
- **Question**: What does the 3-year EBIT path look like under conservative/base/optimistic assumptions for the 3+3+4 grouping?
- **Approach**: Build 3-scenario financial model; Year 1: 3 cities EBIT+; Year 2: +3 cities; Year 3: portfolio EBIT+. Key drivers: AOV improvement, subsidy reduction, partial contraction savings
- **Data**: AX-A1, A2, A3 outputs; 01-problem-definition.md for base numbers
- **Data Status**: ✅ Available (with estimated loss figures as noted)
- **Output**: 3-year EBIT bridge per scenario; breakeven timing
- **Hypothesis**: Even in conservative scenario, 3-city focus achieves EBIT+ by Year 2
- **Priority**: P1
- **Dependencies**: AX-A1, AX-A2, AX-A3 — gating analysis

### AX-A5: Weihai Model Replicability Assessment
- **Question**: Can Weihai's formula (high AOV + low fulfillment cost) be replicated in other cities? What are the preconditions?
- **Approach**: Compare Weihai's driver profile vs. other cities; identify which cities are closest to Weihai's profile; assess AOV uplift levers (category mix, large supermarket depth)
- **Data**: 01-problem-definition.md
- **Data Status**: ✅ Available
- **Output**: Cities ranked by "Weihai-fit" score; AOV uplift pathway per city
- **Hypothesis**: Weihai's model is partially replicable in C7 (Huizhou) and C1 (Xuzhou with AOV improvement), but not in C9/C10 in the short term
- **Priority**: P2
- **Dependencies**: AX-A1, AX-A2 (can run in parallel)

---

## WS-B: Competitive Constraint Boundaries

> **Note**: Research executed by consulting associate via web search. Sources: Meituan/JD.com annual reports, analyst reports (Goldman Sachs, Deutsche Bank, Analysys), industry news.

### AX-B1: Meituan Public Financials & Tier 3-4 Strategy Research
- **Question**: What does Meituan spend on subsidies and R&D per order? What is their disclosed strategy for Tier 3-4 cities?
- **Approach**: Search Meituan 2024 annual report, investor presentations, analyst call transcripts. Search: "Meituan 四五线城市 instant retail subsidy" and "Meituan on-demand R&D cost per order"
- **Data Source**: Meituan IR (hkdata.com), Bloomberg, Goldman/DB analyst reports
- **Data Status**: 🔍 Web search required — executing via subagent
- **Output**: Key findings memo (subsidy floor estimates, Tier 3-4 expansion remarks)
- **Confidence**: Medium — national data only, no city-level disclosure
- **Priority**: P1
- **Dependencies**: None (research-gating for WS-B2)

### AX-B2: JD.com Public Financials & JD Home Delivery Strategy Research
- **Question**: What is JD.com's instant retail strategy in lower-tier cities? How does their到家 model compete?
- **Approach**: Search JD.com 2024 annual report, JD到家 investor materials,Analysys易观 report on instant retail market share
- **Data Source**: JD.com IR,Analysys, iiMedia
- **Data Status**: 🔍 Web search required — executing via subagent
- **Output**: Key findings memo (competitive intensity in Tier 3-4, JD到家差异化 positioning)
- **Confidence**: Medium
- **Priority**: P1
- **Dependencies**: AX-B1 (can run in parallel)

### AX-B3: Competitive Intensity Scenario Analysis
- **Question**: How do different competitive scenarios constrain Instant Retail's subsidy reduction options?
- **Approach**: Synthesize AX-B1+B2 findings into 3 competitive scenarios (high/medium/low). For each: estimate maximum feasible subsidy reduction, identify Instant Retail's response options, flag trigger points
- **Data**: AX-B1, AX-B2 research outputs
- **Data Status**: Pending AX-B1/B2
- **Output**: 3×3 scenario matrix (competitive intensity × internal improvement); subsidy floor per scenario
- **Hypothesis**: Even in high-competition scenario, some subsidy reduction is feasible if targeted at low-value users only
- **Priority**: P1
- **Dependencies**: AX-B1, AX-B2 — gating analysis

---

## WS-C: Subsidy Precision Opportunity

### AX-C1: Subsidy Efficiency Diagnostic
- **Question**: How is the current 4.2元/order average subsidy distributed across city and user quality tiers?
- **Approach**: Cross-city comparison of subsidy per order vs. high-value user %; identify which cities have worst subsidy efficiency
- **Data**: 01-problem-definition.md (subsidy and user % per city)
- **Data Status**: ✅ Available
- **Output**: Subsidy efficiency ranking table; "waste rate" proxy per city
- **Finding to confirm**: C10 has highest subsidy (4.9元) + lowest high-value users (15%) = worst efficiency
- **Priority**: P1
- **Dependencies**: None

### AX-C2: High-Value User Improvement Potential Analysis
- **Question**: What does the Weihai (26%) vs. Ganzhou (15%) gap tell us about improvement potential?
- **Approach**: Compare user and city characteristics between Weihai and Ganzhou; identify structural drivers of the 11pp gap (category mix? large supermarket depth? city demographics? subsidy targeting?)
- **Data**: 01-problem-definition.md; **Known Gap**: no user retention curves or cohort data
- **Data Status**: ⚠️ Partial —断面 data available; longitudinal data missing
- **Output**: Gap decomposition; qualitative improvement pathway; improvement ceiling estimate
- **Hypothesis**: 11pp gap is partially attributable to category mix (Weihai has more到家快消, less restaurant) and large supermarket depth — both actionable within 12 months
- **Priority**: P1
- **Dependencies**: AX-A1 (can run in parallel)

### AX-C3: Subsidy Reallocation Scenario Analysis
- **Question**: What is the financial impact of reallocating subsidy from low-value to high-value users under each competitive scenario?
- **Approach**: Model 3 scenarios (conservative/base/optimistic) for subsidy reallocation over 12 months. Conservative: maintain current subsidy for high-value users only, reduce low-value by 10%; base: reduce low-value by 20%, increase high-value retention incentive; optimistic: full reallocation. Financial impact: delta to annual subsidy spend × effect on high-value user %
- **Data**: AX-C1, AX-C2 outputs; AX-B3 competitive ceiling inputs
- **Data Status**: ⚠️ Model inputs partial — retention curves unknown (known gap)
- **Output**: Subsidy savings range per scenario; high-value user % trajectory per scenario
- **Note**: Will present as "directional estimate with explicit assumptions" — not a precise prediction
- **Priority**: P1
- **Dependencies**: AX-C1, AX-C2, **AX-B3** (competitive ceiling gates the scenarios)

---

## Data Inventory

| Data Item | Source | Status | Notes |
|-----------|--------|--------|-------|
| 10-city AOV, order volume, costs | 01-problem-definition.md | ✅ Have | Primary data source |
| City-level loss estimates | 01-problem-definition.md | ⚠️ Have | Estimated by CSO, not actuals |
| High-value user % by city | 01-problem-definition.md | ✅ Have | 15-26% range |
| Large supermarket % by city | 01-problem-definition.md | ✅ Have | 12-23% range |
| Category mix by city | 01-problem-definition.md | ✅ Have | % for 生鲜/餐饮/到家快消 |
| City open year, market share | 01-problem-definition.md | ✅ Have | 2018-2022 range |
| Monthly / quarterly trends | None | ❌ Unavailable | Do not estimate |
| User retention / repurchase curves | None | ❌ Unavailable | Known gap — use scenario ranges |
| Fixed cost breakdown | None | ❌ Unavailable | Use estimated loss as proxy |
| Meituan Tier 3-4 subsidy data | Public financials / analyst reports | 🔍 Need | Executing via subagent |
| JD.com instant retail data | Public financials | 🔍 Need | Executing via subagent |
| Competitive intensity in target cities | Industry reports | 🔍 Need | Proxy approach |

---

## Timeline (May 1–3, Analysis Phase)

| Date | Focus | Deliverable |
|------|-------|-------------|
| **May 1** | WS-A: Run A1, A2, A3 in parallel | Comparative tables, cost-benefit analysis |
| **May 2** | WS-A: A4 (gating) + A5; WS-B: B1+B2 research | EBIT scenario model; competitive intel memo |
| **May 3** | WS-B: B3; WS-C: C1, C2, C3 | Scenario matrices; findings document |
| **May 4–5** | Integration, cross-review, PPT drafting | — |

**Note**: WS-A analyses are fully data-ready and can launch immediately. WS-B is the pacing item — research subagent fires on May 1 so findings are ready for AX-B3 on May 2.

---

## Metadata

- Step: 4
- Status: draft
- Created: 2026-04-30
- Engagement folder: /Users/minimx/Library/Mobile Documents/com~apple~CloudDocs/Bainsight/InstantRetail/Tier3-4Strategy
- Competition deadline: 2026-05-06
- Analysis deadline: 2026-05-03 (EOB)
