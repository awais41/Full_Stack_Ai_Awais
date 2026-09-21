import pandas as pd

df = pd.read_csv('startup_growth_investment_data__1_.csv')

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

print(df['Industry'].nunique())
print(df['Industry'].value_counts())

# selecting columns
print(df['Startup Name'])
print(df[['Startup Name', 'Industry', 'Country']])

# filtering
germany = df[df['Country'] == 'Germany']
print(germany.shape)

saas = df[df['Industry'] == 'SaaS']
print(saas.shape)

combo = df[(df['Country'] == 'Germany') & (df['Industry'] == 'SaaS')]
print(combo)

# loc/iloc
print(df.loc[5, 'Startup Name'])
print(df.iloc[5, 6])
print(df.loc[0:3, 'Industry':'Investment Amount (USD)'])

# adding a row just to see how it works
new_row = ['Test Startup', 'AI', 3, 1000000.0, 5000000.0, 5, 'USA', 2023, 42.0]
df.loc[len(df.index)] = new_row
print(df.tail())

# removing it again, was just testing
df = df.drop(df.index[-1])
print(df.shape)

# rename clunky column names
df.rename(columns={
    'Investment Amount (USD)': 'investment_usd',
    'Valuation (USD)': 'valuation_usd',
    'Growth Rate (%)': 'growth_rate_pct'
}, inplace=True)

# query()
selected = df.query('Country == "Germany" or Industry == "Fintech"')
print(selected[['Startup Name', 'Country', 'Industry']])
print(len(selected))

# missing data check - this dataset happens to be fully populated
print(df['investment_usd'].isnull().sum())
print(df.isnull().sum())

# sorting
print(df.sort_values('Startup Name').head())
print(df.sort_values(['Industry', 'Country'], ascending=[True, False]).head(10))

# groupby
country_counts = df.groupby('Country')['Startup Name'].count()
print(country_counts.sort_values(ascending=True).head(10))

print(df.groupby('Industry')['Startup Name'].count().sort_values(ascending=False))

# agg + pivot
industry_stats = df.groupby('Industry').agg({'Country': 'nunique'})
industry_stats = industry_stats.reset_index()
industry_stats = industry_stats.rename(columns={'Country': 'countries_present_in'})
print(industry_stats.sort_values('countries_present_in', ascending=False).head(10))

pivot = df.pivot_table(values='Startup Name', index='Industry', columns='Country', aggfunc='count')
print(pivot.head())

pivot2 = df.pivot_table(values='investment_usd', index='Industry', columns='Country', aggfunc='mean')
print(pivot2.head())

# string operations
print(df['Country'].str.lower().head())

tech_places = df[df['Industry'].str.contains('Tech', case=False, na=False)]
print(len(tech_places))
print(tech_places['Industry'].value_counts().head(10))

# naming style demo - normalizing hyphenation e.g. E-commerce vs Ecommerce
df['industry_clean'] = df['Industry'].str.replace("-", "", regex=False)
print(df[df['industry_clean'].str.contains('Ecommerce', case=False, na=False)]['Industry'].value_counts())

# merge example - small lookup table mapping country to region
region_lookup = pd.DataFrame({
    'Country': ['USA', 'Canada', 'Germany', 'UK', 'France', 'India', 'China', 'Singapore', 'Brazil', 'Australia'],
    'region': ['North America', 'North America', 'Europe', 'Europe', 'Europe', 'Asia', 'Asia', 'Asia', 'South America', 'Oceania']
})
merged = pd.merge(df, region_lookup, on='Country', how='left')
print(merged[['Startup Name', 'Country', 'region']].head())
print(merged['region'].isnull().sum())

# apply/map
df['name_length'] = df['Startup Name'].apply(len)
print(df[['Startup Name', 'name_length']].head())

def classify(industry):
    return 'Tech-related' if 'tech' in industry.lower() or industry in ('AI', 'SaaS', 'Blockchain') else 'Other'

df['category'] = df['Industry'].apply(classify)
print(df['category'].value_counts())

df['location_summary'] = df.apply(lambda row: f"{row['Startup Name']} - {row['Industry']}, {row['Country']}", axis=1)
print(df['location_summary'].head())

region_map = {'USA': 'North America', 'Canada': 'North America', 'Germany': 'Europe'}
df['region_mapped'] = df['Country'].map(region_map)
print(df[['Country', 'region_mapped']].head(10))

# duplicates
print(df.duplicated().sum())
print(df.duplicated(subset=['Startup Name']).sum())

dupes = df[df.duplicated(subset=['Startup Name'], keep=False)]
print(dupes[['Startup Name', 'Country', 'Industry']].sort_values('Startup Name').head(10))

df_clean = df.drop_duplicates(subset=['Startup Name'])
print(df.shape, df_clean.shape)

# reshape - long format from the pivot table above
long_format = pivot.reset_index().melt(id_vars='Industry', var_name='Country', value_name='startup_count')
print(long_format.dropna().head(10))

# correlation
print(df[['investment_usd', 'valuation_usd', 'growth_rate_pct', 'Number of Investors']].corr())

print(df['Country'].describe())
print(df['Industry'].describe())

# summary
top_country = country_counts.idxmax()
print("country with most startups:", top_country, "-", country_counts.max())

top_industry = df['Industry'].value_counts().idxmax()
print("most common industry:", top_industry)

tech_pct = len(tech_places) / len(df) * 100
print(f"percentage of startups with 'Tech' in the industry name: {tech_pct:.1f}%")