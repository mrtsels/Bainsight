---
id: 04-work-plan
type: work-plan
step: 4
title: "O2O Strategy Work Plan"
status: draft
addresses: "03-priority-matrix.md"
workplan_file: "04-work-plan.xlsx"
workstreams:
  - id: WS1
    name: "City Portfolio Logic & Prioritization"
    owner: "Team"
    effort: "High"
    focus_area: "03-priority-matrix.md#fa-portfolio"
  - id: WS2
    name: "Fulfillment & Operating Model Pivot"
    owner: "Team"
    effort: "High"
    focus_area: "03-priority-matrix.md#fa-operating-model"
  - id: WS3
    name: "Subsidy Optimization & 3-Year Break-Even Path"
    owner: "Team"
    effort: "Medium"
    focus_area: "03-priority-matrix.md#fa-subsidy"
dependencies:
  - "City-level P&L details to determine root causes of profitability gaps."
  - "Competitor density proxies to finalize market exits."
  - "Baseline fulfillment unit economics for alternative models (e.g. flash warehouse) to assess pivot viability."
---

# Work Plan: Instant Retail Co. O2O Strategy

This document outlines the analytical roadmap for answering the Key Question defined in Step 1, utilizing the prioritized areas established in Step 3. The full tactical execution and data inventory are maintained in the accompanying [04-work-plan.xlsx](04-work-plan.xlsx).

## Workplan Overview

### Objective

Translate the three core Priority 1 Focus Areas into actionable modules: a City Prioritization matrix, a Business Model Assessment, and a Bottom-Up Break-Even Path.

### Phase 1: Profitability Diagnostic & City Screening (WS1)

- **Goal:** Unpack the root causes of the losses in the 10 candidate Tier-3/Tier-4 cities. We will categorize cities into Invest, Optimize, or Exit.
- **Key Analysis:**
  - Waterfall diagnostic modeling loss per-order (AOV vs Fulfillment vs Subsidy vs COGS).
  - Multi-factor scoring model mapping Market Attractiveness against Instant Retail Co.'s "Right-to-Win" (MAU, High-Value Users, Growth).
- **Constraints/Data:** Utilizing the internal Excel fact base for all 10 cities; seeking public proxies for competitor local presence.

### Phase 2: Fulfillment Model Pivot (WS2)

- **Goal:** Determine the threshold order density / breakeven logic under competing models (Dark Store vs. Flash Warehouse vs. Third-Party Marketplace).
- **Key Analysis:**
  - Compare fulfillment cost structures per model against local density constraints.
  - Formulate a decision matrix mapping optimal O2O models per city archetype.
- **Constraints/Data:** Relies on estimating fulfillment and variable costs for alternative structures.

### Phase 3: Subsidy Optimization (WS3)

- **Goal:** Design a trajectory for the "Invest" and "Optimize" cities over the next three years to reach profitability.
- **Key Analysis:**
  - Correlating subsidy spend against high-value user share.
  - Subsidy tapering sensitivity showing volume vs. margin trade-offs over 3 years.
- **Constraints/Data:** Requires assumptions around user price elasticity and churn when coupons are reduced.

## Execution Timeline

- **Deadline:** ASAP
- **Deliverable:** The final deliverable output will integrate these three workstreams into a single presentation narrative suitable for the CSO, providing a solid recommendation grounded in the 10-city dataset breakdown.

---

_Refer to [04-work-plan.xlsx](04-work-plan.xlsx) for the detailed worksheet mapping each specific analysis back to required data sources and individual hypotheses._
