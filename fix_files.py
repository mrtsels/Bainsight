import re

# Fix 06-synthesis.md
with open("Instant Retail Co/O2O Strategy/06-synthesis.md", "r") as f:
    syn = f.read()

syn = syn.replace(
    "Pivoting to a Flash Warehouse model (partner picking, platform delivery) drops this to ~¥9/order, structurally pushing our \"Optimize\" and \"Invest\" cities aggressively towards positive unit margins.",
    "Pivoting to a Flash Warehouse model (partner picking, platform delivery) drops this dark store volume cost to ~¥9/order. This yields a blended saving of ~¥1.1 per order across the city, structurally pushing our \"Optimize\" and \"Invest\" cities aggressively towards positive unit margins."
)

syn = syn.replace(
    "Assuming an optimistic elasticity (-0.6) for our 20% high-value user base, volume drops <1% while restoring ¥0.7–1.0 per order directly to the bottom line.",
    "While the absolute order volume from price-sensitive cohorts will drop significantly, this represents an intentional shedding of unprofitable orders. Retaining our inelastic high-value core restores ¥0.7–1.0 per order directly to the bottom line."
)

syn = syn.replace(
    "The exact volume response (elasticity) to subsidy tapering (Insight 3).",
    "The exact volume response to subsidy tapering among the non-core users (Insight 3)."
)

with open("Instant Retail Co/O2O Strategy/06-synthesis.md", "w") as f:
    f.write(syn)

# Fix 07-recommendations.md
with open("Instant Retail Co/O2O Strategy/07-recommendations.md", "r") as f:
    rec = f.read()

rec = rec.replace(
    "By targeting the cuts at price-sensitive cohorts, total volume drops by <1% (optimistic scenario), while margins recover ¥0.7–1.0 per order.",
    "While absolute volume drops as price-sensitive cohorts churn, this constitutes an intentional shedding of unprofitable orders. Margins recover ¥0.7–1.0 per order on the remaining sticky volume."
)

rec = rec.replace(
    "| Halt marketing spend in Xuzhou, Luoyang, Ganzhou | Marketing | Day 1 | ¥0 CAC in exit cities |",
    "| Halt marketing spend in Xuzhou, Luoyang, Ganzhou | Marketing | Day 1 | Halt ~¥5M/month operational burn by Month 3 |"
)

rec = rec.replace(
    "| Reinvest 20% of exit savings into top 4 \"Invest\" cities | Marketing | Month 12 | +15% YoY Revenue Growth locally |",
    "| Absorb Dark Store lease breakages and transition costs with remaining 80% of exit savings | Finance | Month 12 | Smooth P&L transition |\n| Reinvest 20% of exit savings into top 4 \"Invest\" cities | Marketing | Month 12 | +15% YoY Revenue Growth locally |"
)

rec = rec.replace(
    "| Expand categories within Flash Warehouse partners | BD | Year 3 | AOV increases by +10% |",
    "| Expand into bulky electronics and premium liquor within Flash Warehouses | BD | Year 3 | AOV increases by +10% |"
)

rec = rec.replace(
    "recovers margin with <1% volume loss.",
    "recovers margin by intentionally shedding unprofitable volume."
)

rec = rec.replace(
    "• Expand partner categories to capture AOV upside.",
    "• Expand into premium liquor and electronics to capture AOV upside."
)

with open("Instant Retail Co/O2O Strategy/07-recommendations.md", "w") as f:
    f.write(rec)

# Fix 08-slide-storyline.md
with open("Instant Retail Co/O2O Strategy/08-slide-storyline.md", "r") as f:
    story = f.read()

story = story.replace(
    "*Title:* This critical ~¥2/order structural cost reduction pushes the \"Optimize\" and \"Invest\" cities immediately toward positive unit territory.",
    "*Title:* This ~¥2/order drop on dark store volume yields a ~¥1.1 blended saving per order, pushing \"Optimize\" and \"Invest\" cities toward positive unit territory."
)

story = story.replace(
    "*Message:* Tapering subsidies by 20% exclusively on price-sensitive, non-core users acts as a hidden ~1.5% effective price increase.",
    "*Message:* Tapering subsidies by 20% on price-sensitive, non-core users acts as an aggressive repricing to filter out purely opportunistic volume."
)

story = story.replace(
    "*Title:* Under conservative elasticity modeling, this targeted taper drops overall order volume by <1% while recovering ¥0.7–1.0 directly to the margin.",
    "*Title:* While price-sensitive volume will drop, this intentional shedding of unprofitable orders recovers ¥0.7–1.0 directly to the city margin."
)

story = story.replace(
    "*Message:* By Year 2, the newly established baseline allows us to capture long-term AOV growth by expanding partner categories.",
    "*Message:* By Year 2, the newly established baseline allows us to capture long-term AOV growth by expanding into premium liquor, electronics, and bulk FMCG."
)

with open("Instant Retail Co/O2O Strategy/08-slide-storyline.md", "w") as f:
    f.write(story)

