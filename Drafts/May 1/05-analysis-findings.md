---
id: 05-analysis-findings
type: analysis-findings
step: 5
title: "Analysis Findings"
status: draft
addresses: "01-problem-definition.md#kq"
findings:
  - anchor: "05-analysis-findings.md#f-1"
    label: "3 Cities are unviable and should be exited."
    investigates: "04-work-plan.md#ax-ws1-a2"
    branch: "02-issue-tree.md#br-1.1"
    confidence: high
  - anchor: "05-analysis-findings.md#f-2"
    label: "Dark stores are structurally unprofitable in T3/4."
    investigates: "04-work-plan.md#ax-ws2-a2"
    branch: "02-issue-tree.md#br-2.1"
    confidence: high
  - anchor: "05-analysis-findings.md#f-3"
    label: "A 20% subsidy cut accelerates breakeven with negligible volume loss."
    investigates: "04-work-plan.md#ax-ws3-a2"
    branch: "02-issue-tree.md#br-3.2"
    confidence: medium
hypothesis_status:
  - anchor: "05-analysis-findings.md#hs-portfolio"
    hypothesis: "01-problem-definition.md#hyp-1"
    status: confirmed
    evidence: "05-analysis-findings.md#f-1"
    note: "Applying a uniform strategy is failing. Exiting 3 unviable cities stops major cash bleed."
  - anchor: "05-analysis-findings.md#hs-om"
    hypothesis: "01-problem-definition.md#hyp-2"
    status: confirmed
    evidence: "05-analysis-findings.md#f-2"
    note: "Asset-light models (Flash Warehouse) lower unit costs sufficiently to push 'Optimize' cities to breakeven."
  - anchor: "05-analysis-findings.md#hs-subsidy"
    hypothesis: "01-problem-definition.md#hyp-3"
    status: partially_confirmed
    evidence: "05-analysis-findings.md#f-3"
    note: "Tapering subsidies works, but must be targeted securely to avoid higher-than-expected elasticity impacts."
---

# Analysis Findings

## Summary of Key Findings

| #   | Finding                                                                                                                                                                                                       | So What?                                                                                                                                                       | Confidence |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1   | Weihai, Quanzhou, and Huizhou rank as high-priority "Invest" markets with strong penetration and high-value user density. Xuzhou, Luoyang, and Ganzhou are structural laggards.                               | We should divest completely from the bottom 3 cities and reallocate focus exclusively to the remaining 7, halting immediate cash bleed.                        | High       |
| 2   | Dark Store models cost ¥10.5–12.0/order to fulfill. Given an approximate ¥13–14 implied revenue per order (take rate), this leaves almost nothing to cover subsidies and generates constant negative margins. | We must mandate a pivot to Flash Warehouse (¥8.5–9.5/order) or Marketplace models in Tier-3/4. Dark stores require order volumes these cities cannot support.  | High       |
| 3   | Subsidy (currently ¥3.5-4.9/order) tapering by 20% acts as a ~1.5% effective price increase. Assuming an optimistic elasticity of -0.6 for our sticky, high-value users, order volume will drop <1%.          | Smart targeting of subsidy cuts directly recovers ~¥0.7–1.0 per transaction to the bottom line, significantly expediting the 3-year breakeven timeline safely. | Medium     |

## Detailed Findings

### Analysis 1: City Portfolio Logic & Scoring (WS1)

**Question**: Which cities should we Invest, Optimize, or Exit?
**Key Finding**: Applying a Market Attractiveness vs Right-to-Win scoring model reveals 3 runaway failures. Xuzhou, for instance, burns ¥25M annually due to terrible performance on high-value user retention (22%) and supermarket share. Quanzhou, conversely, is already breakeven with a 25% high-value user base and 35% market share.
**Supporting Evidence**: `WS1_Scoring` tab in `05-analyze-workbook.xlsx` (Data from Internal Fact Base).
**So What?**: A blanket approach fails. Exiting the bottom 3 immediately saves over ¥60M in annual burn.
**Hypothesis Status**: **Confirmed**.

### Analysis 2: Fulfillment Model Pivot (WS2)

**Question**: Which operating model breaches the unit economic breakeven threshold fastest?
**Key Finding**: At the current blended fulfillment rate of ~¥10.1/order, we are stuck. A purely Dark Store approach assumes ¥11/order base costs, guaranteeing losses. Switching to a Flash Warehouse approach lowers physical picking and real estate burdens, reducing this to ¥9/order.
**Supporting Evidence**: `WS2_Model_Pivot` tab in `05-analyze-workbook.xlsx` (Assumption Benchmarks derived from city-level facts).
**So What?**: The capital-intensive dark store is fundamentally misaligned with Tier-3/4 order density. We must work with local supermarkets and convenience stores to handle inventory and picking (Flash Warehouse model).
**Hypothesis Status**: **Confirmed**.

### Analysis 3: Subsidy Optimization (WS3)

**Question**: What happens to volume/P&L if we cut subsidies by 20%?
**Key Finding**: A 20% blanket cut recovers ¥0.7 - ¥1.0 in margin per order. Because our cities have an average ~20% "high-value" user set, we can taper subsidies selectively. Under an optimistic demand scenario (-0.6 price elasticity), we absorb only a 0.9% drop in total volume while vastly improving the city-level P&L.
**Supporting Evidence**: `WS3_Subsidy` tab in `05-analyze-workbook.xlsx` (Elasticity scenarios based on team estimates).
**So What?**: Tapering subsidies isn’t just a cost-cut; when mapped precisely to opportunistic users and protecting core users, it acts as a primary profitability lever without triggering a death spiral.
**Hypothesis Status**: **Partially confirmed** (elasticity in reality must be carefully gated and monitored locally).

## Emerging Themes

- **Density is Destiny:** Both structural profitability and business model viability boil down to how fast we can consolidate operations around existing supermarket footprints rather than building our own warehouses.
- **Stop Buying Bad Growth:** The cities burning the most cash are trying to brute-force a Dark Store + High Subsidy combination. This doesn't scale.

## Open Questions

- What is the exact execution timeline to unwind the Dark Store leases in the "Exit" and "Optimize" cities?
- Will competitors (Meituan, JD) aggressively fill the white space left by our taper, shifting our actual elasticity closer to the conservative -2.0 assumption?

## Key Assumptions and Limitations

- **Fulfillment Cost Baseline:** We assumed a generic cost of ¥11 for Dark Stores and ¥9 for Flash Warehouses. This must be validated against real procurement leases if approved.
- **Implied Revenue:** In absence of granular platform P&Ls (e.g. ad revenue vs pure commission), we back-calculated implied gross revenue per order based on reported losses and variable costs.
- **Elasticities:** We assumed an effective price increase of 1.5% driven by a 20% subsidy cut, with elasticities ranging from -0.6 to -2.0. Real-world consumer behavior may be lumpier.
