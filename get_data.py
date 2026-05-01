import pandas as pd
file_path = '/Users/minimx/Library/Mobile Documents/com~apple~CloudDocs/Bainsight/2026_Bain_Cup_Case_Data from Instant Retail Co.xlsx'
df = pd.read_excel(file_path)
print(df.head(10).to_string())
