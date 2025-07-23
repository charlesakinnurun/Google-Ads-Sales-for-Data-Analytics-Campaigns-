import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('dataset/data.csv')

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('-', '_')
)

# Remove $ and convert to float
for col in ['cost', 'sale_amount']:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace('$', '', regex=False)
        .replace('', np.nan)
        .astype(float)
    )

# Standardize date formats
def parse_date(x):
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"):
        try:
            return pd.to_datetime(x, format=fmt)
        except:
            continue
    return pd.NaT

df['ad_date'] = df['ad_date'].apply(parse_date)

# Standardize text columns
def fix_campaign(x):
    x = x.lower().replace(' ', '').replace('_', '')
    if 'dataanalyticscourse' in x:
        return 'DataAnalyticsCourse'
    return 'Data Analytics Course'

df['campaign_name'] = df['campaign_name'].apply(fix_campaign)

def fix_location(x):
    x = str(x).strip().lower()
    if 'hyder' in x:
        return 'Hyderabad'
    return x.capitalize()

df['location'] = df['location'].apply(fix_location)

def fix_device(x):
    x = str(x).strip().lower()
    if 'desk' in x:
        return 'Desktop'
    if 'mob' in x:
        return 'Mobile'
    if 'tab' in x:
        return 'Tablet'
    return x.capitalize()

df['device'] = df['device'].apply(fix_device)

# Standardize keywords
df['keyword'] = df['keyword'].str.strip().str.lower()

# Fill missing numeric values with median
for col in ['clicks', 'impressions', 'cost', 'leads', 'conversions', 'conversion_rate', 'sale_amount']:
    if df[col].dtype in [np.float64, np.int64, float, int]:
        df[col] = df[col].fillna(df[col].median())

# Save cleaned data
df.to_csv('dataset/data_cleaned.csv', index=False)
print("Data cleaned and saved to dataset/data_cleaned.csv")