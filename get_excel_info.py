import pandas as pd
file_path = '/Users/minimx/Library/Mobile Documents/com~apple~CloudDocs/Bainsight/2026_Bain_Cup_Case_Data from Instant Retail Co.xlsx'
try:
    xl = pd.ExcelFile(file_path)
    print("Sheets:", xl.sheet_names)
    for sheet in xl.sheet_names:
        df = xl.parse(sheet, nrows=5)
        print(f"\nSheet '{sheet}' columns:")
        print(df.columns.tolist())
except Exception as e:
    print("Error:", e)
