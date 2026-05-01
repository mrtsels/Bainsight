import pandas as pd

# Tab 1: Summary
summary_data = {
    "Project Name": ["Instant Retail Co. O2O Strategy"],
    "Key Question": ["How can Instant Retail Co. turn its currently unprofitable Tier-3 and Tier-4 operations into a sustainable, profit-contributing engine?"],
    "Date": ["April 30, 2026"],
    "Timeline": ["ASAP"]
}
summary_df = pd.DataFrame(summary_data)

workstreams_data = {
    "Workstream Name": [
        "WS1: City Portfolio Logic & Prioritization", 
        "WS2: Fulfillment & Operating Model Pivot", 
        "WS3: Subsidy Optimization & 3-Year Break-Even"
    ],
    "# Analyses": [3, 2, 3],
    "Effort": ["High", "High", "Medium"],
    "Milestone": ["City Scoring Matrix & Selection", "Business Model Comparison", "Unit Economics Break-Even Model"]
}
workstreams_df = pd.DataFrame(workstreams_data)

# Tab 2: Detailed Analysis Plan
plan_data = {
    "ID": ["WS1-A1", "WS1-A2", "WS1-A3", "WS2-A1", "WS2-A2", "WS3-A1", "WS3-A2", "WS3-A3"],
    "Workstream": [
        "1. City Portfolio", "1. City Portfolio", "1. City Portfolio", 
        "2. Operating Model", "2. Operating Model", 
        "3. Subsidy & Break-Even", "3. Subsidy & Break-Even", "3. Subsidy & Break-Even"
    ],
    "Analysis Name": [
        "Profitability Diagnostic", 
        "City Scoring Model", 
        "Competitor Heatmap Proxy",
        "Fulfillment Cost Density Analysis", 
        "Business Model Scenario Comparison",
        "Subsidy vs. High-Value User Correlation",
        "Subsidy Tapering Sensitivity",
        "3-Year Bottom-Up Break-Even Path"
    ],
    "Question to Answer": [
        "What are the root causes of per-order losses in each city?",
        "Which cities should we Invest, Optimize, or Exit?",
        "Where is competitor intensity lowest?",
        "What is the gap between current order density and viable fulfillment costs?",
        "Dark Store vs Flash Warehouse vs Marketplace - which breakevens fastest?",
        "Are subsidies driving sticky users or just opportunistic volume?",
        "What happens to volume/P&L if we cut subsidies by 20-30%?",
        "When will priority cities flip to profitability?"
    ],
    "Data Needed": [
        "AOV, Fulfillment, Subsidy per order",
        "Macro data, MAU, O2O share, growth",
        "External reports on Meituan/JD presence",
        "Pop density, Order vol, Fulfillment cost",
        "Fulfillment cost benchmarks per model",
        "High-value user %, Subsidy per order",
        "Price elasticity estimates",
        "Projected AOV, orders, costs"
    ],
    "Data Source": ["Internal Excel", "Internal Excel", "Public Reports", "Internal Excel", "Internal Excel & Benchmarks", "Internal Excel", "Assumptions", "Model Output"],
    "Output Format": ["Waterfall Chart", "2x2 Matrix & Table", "Map / Table", "Scatter Plot", "Decision Matrix & P&L", "Correlation Chart", "Sensitivity Table", "Timeline & Waterfall"],
    "Priority": ["P1", "P1", "P2", "P1", "P1", "P1", "P2", "P1"],
    "Status": ["Not Started", "Not Started", "Not Started", "Not Started", "Not Started", "Not Started", "Not Started", "Not Started"]
}
plan_df = pd.DataFrame(plan_data)

# Tab 3: Data Inventory
data_inv = {
    "Data Item": [
        "City-level P&L and Unit Economics (AOV, Fulfillment, Subsidy)",
        "City Scale & User Base (Orders, MAU, High-Value %)",
        "Market Position (Market Share, YoY Growth)",
        "Macro Context (Population, GDP, Income)",
        "Competitor Presence (Meituan, Alibaba, JD)",
        "Fulfillment Model Benchmarks (Dark Store vs Flash vs Marketplace)"
    ],
    "Source": ["Internal Excel", "Internal Excel", "Internal Excel", "Internal Excel", "External Search", "External/Assumptions"],
    "Status": ["Available", "Available", "Available", "Available", "Needed", "Needed"],
    "Notes": ["Complete for all 10 cities", "Complete for all 10 cities", "Complete", "Complete", "Need proxies if direct data unavailable", "Critical for WS2"]
}
inv_df = pd.DataFrame(data_inv)

with pd.ExcelWriter("Instant Retail Co/O2O Strategy/04-work-plan.xlsx") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False, startrow=0)
    workstreams_df.to_excel(writer, sheet_name="Summary", index=False, startrow=6)
    plan_df.to_excel(writer, sheet_name="Detailed Analysis Plan", index=False)
    inv_df.to_excel(writer, sheet_name="Data Inventory", index=False)

print("Excel generated successfully.")
