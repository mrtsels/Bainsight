---
id: 03-priority-matrix
type: priority-matrix
step: 3
title: "Priority Matrix"
status: draft
addresses: "01-problem-definition.md#kq"
prioritizes:
  - "02-issue-tree.md#br-1.1"
  - "02-issue-tree.md#br-2.1"
  - "02-issue-tree.md#br-3.2"
focus_areas:
  - anchor: "03-priority-matrix.md#fa-portfolio"
    label: "City Portfolio Logic (Invest/Optimize/Exit)"
    tier: P1
    branch: "02-issue-tree.md#br-1.1"
  - anchor: "03-priority-matrix.md#fa-operating-model"
    label: "Fulfillment & Operating Model Pivot"
    tier: P1
    branch: "02-issue-tree.md#br-2.1"
  - anchor: "03-priority-matrix.md#fa-subsidy"
    label: "Subsidy Optimization & High-Value User Retention"
    tier: P1
    branch: "02-issue-tree.md#br-3.2"
parked:
  - branch: "02-issue-tree.md#br-3.3.2"
    reason: "Supply chain integration (like deep supermarket tech tie-ins) requires long BD cycles; not a short-term P&L lever."
  - branch: "02-issue-tree.md#br-1.2"
    reason: "Granular competitor intelligence (e.g., Meituan local subsidy budgets) is impossible to accurately acquire given time constraints."
---

# Prioritization: Instant Retail Co. O2O Strategy

## Priority Assessment

| Issue Branch                        | Impact | Feasibility | Priority   | Rationale                                                                                                                                                                 |
| ----------------------------------- | ------ | ----------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1.1 City Portfolio Strategy**     | High   | High        | **P1**     | Halting investment in all 10 cities and picking winners is the fastest way to stanch ₹10-25M per-city losses. We have internal data for all 10 to model this immediately. |
| **3.2 Subsidy Efficiency**          | High   | High        | **P1**     | Subsidies directly hurt unit economics. Reallocating marketing away from non-sticky users to high-value cohorts requires no capital and moves the needle fast.            |
| **2.1 Fulfillment Model Alignment** | High   | Medium      | **P1**     | Dark stores demand huge density. Moving to asset-light (flash warehouse/marketplace) radically lowers the breakeven threshold. Feasible through scenario modeling.        |
| **3.1 Category Mix / AOV**          | Medium | Medium      | **P2**     | Influencing consumer basket size takes time. Good for baseline modeling (e.g., assuming modest +5% AOV growth), but shouldn't be the core strategic bet.                  |
| **3.3.1 Density & Routing Ops**     | Medium | Low         | **P3**     | Highly operational. Hard to model routing AI improvements comprehensively from a strategic viewpoint without deep operational process data.                               |
| **1.2 Competitor Defensibility**    | High   | Low         | **Parked** | Granular rival intelligence per Tier-3 city is extremely hard to gather and limits our ability to make data-backed assumptions. We will use public proxies instead.       |
| **3.3.2 Deep Supply-Chain Tie-Ins** | High   | Low         | **Parked** | Building new tech alignments with regional supermarkets is high-latency and depends on third parties. Can't rely on it to fix 12-18 month cash burn.                      |

## Focus Areas (Deep Analysis)

### 1. <a id="fa-portfolio"></a>City Portfolio Logic (Invest/Optimize/Exit)

- **Why**: Determining which out of the 10 cities have the right structural advantages (density, existing high-value user base) defines exactly where to execute our "How to Win" strategies. This serves as the foundation of the 15-slide deck.
- **Hypothesis to test**: Applying a uniform strategy across all T3-T4 cities is failing. Segmenting the 10 cities will identify 2-4 candidates suitable for asset-light pivots, and 2-4 candidates where we must halt expansion entirely to preserve runway.
- **Estimated effort**: High. Requires a rapid cross-sectional analysis of evaluating all 10 cities against criteria constraints.

### 2. <a id="fa-subsidy"></a>Subsidy Optimization & High-Value User Retention

- **Why**: "Spending our way to scale" is explicitly prohibited by leadership. We need to identify a sustainable path out of the subsidy trap to reach profitability.
- **Hypothesis to test**: 80% of our current subsidy bleed targets opportunistic, low-retention buyers. Redirecting targeted CAC bounds will shrink per-order losses without decimating the loyal core.
- **Estimated effort**: Medium. We will use the provided AOV and subsidy rates to model before-and-after margins per transaction.

### 3. <a id="fa-operating-model"></a>Fulfillment & Operating Model Pivot

- **Why**: Since we cannot manipulate volume magically in Tier 3/4, we must structurally attack fixed fulfillment costs. Asset-heavy dark stores require volume that isn't there.
- **Hypothesis to test**: Transitioning to an asset-light model (e.g. flash warehouse or a marketplace setup) in borderline 'Optimize' cities reduces the required break-even order volume to attainable levels.
- **Estimated effort**: High. P&L baseline comparison between a Dark Store VS. Marketplace unit economic model.

## Parking Lot

- **Extensive Competitor Modeling**: We will acknowledge Meituan/JD in the narrative, but we will not attempt to dimension their precise capabilities or subsidy depths in each specific T3 market.
- **Long-term Supply Chain Architecture**: We'll focus strictly on levers within the immediate control of the commercial teams (marketing, fulfillment structure, go/no-go logic) rather than 3-year BD pipeline expansions.

## Implications for Work Plan

For **Step 4 (Work Plan)**, the team must split into three parallel workstreams:

1. **City Assessment Model**: Build the metric grading matrix using internal data for the 10 cities.
2. **Alternative P&L Scenarios**: Sketch out unit economics for Dark Store vs Flash Warehouse.
3. **Subsidy Re-Alignment**: Calculate the theoretical margin recovery of capping CAC/volume-based coupons across the portfolio.
