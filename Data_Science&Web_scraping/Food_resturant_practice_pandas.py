

import pandas as pd 
df = pd.read_csv('FastFoodRestaurants.csv')

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

print(df['name'].nunique())
print(df['name'].value_counts())

# selecting columns 
print(df['name'])
print(['name','city','province'])

# filtering - this dataset has case sensitivity issues so being careful here
chicago = df[df['city'] == 'Chicago']
print(chicago.shape)

mcd = df[df['name'] == "McDonald's"]
print(mcd.shape)

combo = df[(df['city']=='Chicago') & (df['name'] == "McDonald's")]
print(combo)

# loc/iloc

print(df.loc[5,'name'])
print(df.iloc[5,6])
print(df.loc[0:3,'city':'name'])

# adding a row just to see it hows it works 

new_row = ['999 Test Ave', 'Test City', 'US', 'test-key-001', 40.0, -75.0,
           'Test Restaurant', '00000', 'TS', 'http://test.com']
df.loc[len(df.index)] = new_row
print(df.tail())

# removing its again was just testing
df.drop(df.index[-1])
print(df.shape)

# rename postalcode/websites are kind of clunky names 
df.rename(columns={'postalcode':'postal_code'}, inplace = True)
df.rename(mapper={'websites': 'website_urls'} , axis=1,inplace=True)

# query() - postal_code is text here so can't do > comparisons on it directly
selected = df.query('city == "Chicago" or province == "IL"')
print(selected[['name','city' ,'province']])
print(len(selected))

# missing data - only website_urls has missing values in this one
print(df['website_urls'].isnull().sum())
print(df[df['website_urls'].isnull()][['name','city']].head())
df['website_urls'] = df['website_urls'].fillna('NO website listed')
print(df['website_urls'].isnull().sum())



# sorting
print(df.sort_values('name').head())
print(df.sort_values(['province' , 'city'],ascending = [True,False]).head(10))

# groupby - this is where the dataset gets interesting
city_counts = df.groupby('city')['name'].count() 
print(city_counts.sort_values(ascending = True).head(10))

print(df.groupby('province')['name'].count().sort_values(ascending=False))

# agg + pivot

brand_stats = df.groupby('name').agg({'city': 'nunique'})
brand_stats = brand_stats.reset_index()
brand_stats = brand_stats.rename(columns={'city': 'cities_present_in'})
print(brand_stats.sort_values('cities_present_in', ascending=False).head(10))

pivot = df.pivot_table(values='name', index='province', columns='country', aggfunc='count')
print(pivot.head())
 
# province vs price_category (agar humne banayi thi apply() mein)
# ya phir bare kaam ka:
pivot2 = df.pivot_table(values='address', index='province', columns='name', aggfunc='count')
print(pivot2.head())
# string operations - this is the messy part of this dataset
print(df['city'].str.lower().head())

pizza_places = df[df['name'].str.contains('pizza', case = False , na = False)]
print(len(pizza_places))
print(pizza_places['name'].value_counts().head(10))

# there's a naming inconsistency issue here - dominos vs domino's etc
df['name_clean'] = df['name'].str.replace("'","", regex = False)
print(df[df['name_clean'].str.contains('Dominos',case = False, na = False)]['name'].value_counts())

# merge example - small lookup table mapping province to region
region_lookup = pd.DataFrame({
    'province': ['IL', 'NY', 'CA', 'TX'],
    'region': ['Midwest', 'Northeast', 'West', 'South']
})
merged = pd.merge(df, region_lookup, on='province', how='left')
print(merged[['name', 'province', 'region']].head())
print(merged['region'].isnull().sum())


# apply/map
df['name_length'] = df['name'].apply(len)
print(df[['name','name_length']].head())

def classify(name):
    return'Pizza Place' if 'pizza' in name.lower() else 'other'

df['category'] = df['name'].apply(classify)
print(df['category'].value_counts())

df['location_summary'] = df.apply(lambda row: f"{row['name']} - {row['city']}, {row['province']}", axis=1)
print(df['location_summary'].head())
 
province_map = {'IL': 'Illinois', 'NY': 'New York', 'CA': 'California'}
df['province_full'] = df['province'].map(province_map)
print(df[['province', 'province_full']].head(10))

# duplicates - real question here is whether any restaurant location got listed twice
print(df.duplicated().sum())
print(df.duplicated(subset=['name','address']).sum())

dupes = df[df.duplicated(subset=['name','address'],keep=False)]

print(dupes[['name', 'address', 'city']].sort_values('name').head(10))
 
df_clean = df.drop_duplicates(subset=['name', 'address'])
print(df.shape, df_clean.shape)
# reshape - long format from the pivot table above

long_format = pivot.reset_index().melt(id_vars = 'province', var_name = 'country',value_name = 'resturant_count')
print(long_format.dropna().head(10))


#  correlation - not much numeric data here besides lat/long which isn't
# really meaningful to correlate, but showing the syntax anyway
print(df[['latitude', 'longitude']].corr())
 
print(df['city'].describe())
print(df['name'].describe())
 
 
# summary
top_city = city_counts.idxmax()
print("city with most fast food restaurants:", top_city, "-", city_counts.max())
 
top_brand = df['name'].value_counts().idxmax()
print("most common restaurant brand:", top_brand)
 
pizza_pct = len(pizza_places) / len(df) * 100
print(f"percentage of restaurants with pizza in the name: {pizza_pct:.1f}%")
 