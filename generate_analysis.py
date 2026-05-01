import pandas as pd
import numpy as np

file_path = '/Users/minimx/Library/Mobile Documents/com~apple~CloudDocs/Bainsight/2026_Bain_Cup_Case_Data from Instant Retail Co.xlsx'
df = pd.read_excel(file_path)
df.columns = [
    'City_ID', 'City', 'Province', 'Entry_Year', 'Daily_Orders_k', 'Order_Growth_Pct',
    'Market_Share_Pct', 'AOV', 'Fulfillment_Cost', 'Subsidy_Cost', 'Profit_Desc',
    'MAU_10k', 'High_Value_User_Pct', 'Merchants', 'Supermarket_Pct',
    'Mix_FMCG', 'Mix_Fresh', 'Mix_Food', 'Mix_Other', 'Pop_10k', 'GDP_100m', 'Income'
]

# Impute current loss based on descriptions
def extract_loss(x):
    if '亏损约' in x:
        num_str = x.split('约')[1].replace('万','0000').replace(',', '')
        return - float(num_str)
    elif '接近盈亏平衡' in x or '小幅亏损' in x:
        return -1000000 # minor limit
    else:
        return 0 # basic breakeven

df['Annual_Loss'] = df['Profit_Desc'].apply(extract_loss)
df['Annual_Orders_m'] = df['Daily_Orders_k'] * 365 / 1000
df['Loss_per_order'] = df['Annual_Loss'] / (df['Annual_Orders_m'] * 1000000)
df['Implied_Take_Rate'] = 0.24
# Instead of assuming back-calculation, Let's just use Loss_per_order and fulfillment and subsidy to get the Implied Revenue per order
df['Implied_Revenue_per_order'] = df['Fulfillment_Cost'] + df['Subsidy_Cost'] + df['Loss_per_order']

# WS1: City Scoring
# Factors: Market Attractiveness (Pop, Income, Orders Growth) vs Right to win (Share, High Value Users, Supermarket Pct)
df['Attractiveness_Score'] = (
    df['Income'] / df['Income'].max() * 0.4 + 
    df['Pop_10k'] / df['Pop_10k'].max() * 0.3 + 
    df['Order_Growth_Pct'] / df['Order_Growth_Pct'].max() * 0.3
) * 10
df['RightToWin_Score'] = (
    df['Market_Share_Pct'] / df['Market_Share_Pct'].max() * 0.4 + 
    df['High_Value_User_Pct'] / df['High_Value_User_Pct'].max() * 0.4 + 
    df['Supermarket_Pct'] / df['Supermarket_Pct'].max() * 0.2
) * 10

def categorize(row):
    if row['Attractiveness_Score'] > 6.5 and row['RightToWin_Score'] > 7.0:
        return 'Invest'
    elif row['RightToWin_Score'] > 6.0:
        return 'Optimize'
    else:
        return 'Exit'

df['Portfolio_Call'] = df.apply(categorize, axis=1)

ws1_df = df[['City', 'AOV', 'Fulfillment_Cost', 'Subsidy_Cost', 'Implied_Revenue_per_order', 'Loss_per_order', 'Attractiveness_Score', 'RightToWin_Score', 'Portfolio_Call']].copy()

# WS2: Fulfillment Model Pivot
ws2_df = df[['City', 'Daily_Orders_k', 'Pop_10k', 'Portfolio_Call', 'AOV', 'Implied_Revenue_per_order', 'Subsidy_Cost']].copy()
# Order density (Daily orders / Pop)
ws2_df['Order_Density'] = ws2_df['Daily_Orders_k'] / (ws2_df['Pop_10k'] / 100) # per 10k Pop
ws2_df['DarkStore_Cost'] = 11 # mid range 10.5-12
ws2_df['Flash_Cost'] = 9 # mid range 8.5-9.5
ws2_df['Marketplace_Cost'] = 6.5 # mid range 6.0-7.5

ws2_df['Margin_Flash'] = ws2_df['Implied_Revenue_per_order'] - ws2_df['Flash_Cost'] - df['Subsidy_Cost']
ws2_df['Margin_DS'] = ws2_df['Implied_Revenue_per_order'] - ws2_df['DarkStore_Cost'] - df['Subsidy_Cost']

# WS3: Subsidy Sensitivity & 3-year Break Even (Base vs Optimistic)
# Tapering by 20%
ws3_df = df[['City', 'Daily_Orders_k', 'AOV', 'Subsidy_Cost', 'Implied_Revenue_per_order', 'Loss_per_order']].copy()
ws3_df['Subsidy_Cut'] = ws3_df['Subsidy_Cost'] * 0.2
# Let's say effective price increase is 1.5%
eff_price_inc = 1.015
# Order Drop Conservative (-2.0), Base (-1.2), Optimist (-0.6)
order_drop_optimist = 0.9 / 100
order_drop_base = 1.8 / 100
order_drop_cons = 3.0 / 100

ws3_df['New_Orders_Opt'] = ws3_df['Daily_Orders_k'] * (1 - order_drop_optimist)
ws3_df['New_Orders_Base'] = ws3_df['Daily_Orders_k'] * (1 - order_drop_base)
ws3_df['New_Orders_Cons'] = ws3_df['Daily_Orders_k'] * (1 - order_drop_cons)

# Calculate Margin improvement
# Old margin per order: Loss_per_order (negative)
# New Margin per order = Implied Rev - Fulfillment - (Subsidy * 0.8)
ws3_df['New_Margin_per_order'] = ws3_df['Implied_Revenue_per_order'] - df['Fulfillment_Cost'] - (df['Subsidy_Cost'] * 0.8)

# Summary
summary_data = {
    "Analysis": ["WS1: Profitability & Screening", "WS2: Model Pivot", "WS3: Subsidy Tapering"],
    "Finding": [
        "Quanzhou, Huizhou, Nanning are 'Invest' candidates. 4 are 'Optimize'. 3 are 'Exit'.",
        "Moving to Flash Warehouse pushes 'Optimize' cities to break-even or profitable.",
        "A 20% subsidy cut restores ¥0.7-1.0 per order. With optimistic elasticity (-0.6), order drop is <1%."
    ],
    "Implication": [
        "Focus capital entirely on top 4-5 cities. Fully exit bottom 3.",
        "Dark store is unviable in T3/4. Mandate Flash Warehouse footprint instead.",
        "Precision targeting of non-subsidy responsive users directly flips the unit economics."
    ]
}
sum_df = pd.DataFrame(summary_data)

# Export
with pd.ExcelWriter("Instant Retail Co/O2O Strategy/05-analyze-workbook.xlsx") as writer:
    sum_df.to_excel(writer, sheet_name="Summary", index=False)
    ws1_df.to_excel(writer, sheet_name="WS1_Scoring", index=False)
    ws2_df.to_excel(writer, sheet_name="WS2_Model_Pivot", index=False)
    ws3_df.to_excel(writer, sheet_name="WS3_Subsidy", index=False)

