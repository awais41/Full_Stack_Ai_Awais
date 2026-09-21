import pandas as pd
df = pd.read_csv('FastFoodRestaurants.csv' , delimiter = ',' )

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.info())     
print(df['name'].value_counts())
print(df['name'].nunique())


# Selecting & Filtering Data

df['name']
df[['name','city']]
# 2. Filtering — condition ke hisaab se rows nikalna:
df[df['city'] == 'Chicago']
df[df['name'] == "McDonald's"]

# 3. Multiple conditions — & (and) aur | (or) use karein:

df[(df['city'] == 'Chicago') & (df['name'] == "McDonald's")]

# loc and iloc
print(df.loc[5, 'name'])
print(df.iloc[5,  6])



#  Missing values dhoondna
df.isnull() 
          #Ye poore DataFrame ko check karta hai — har cell ke liye True (agar missing hai) ya False (agar value hai) return karta hai.

df.isnull().sum()
          # Ye har column mein kitni missing values hain, unka total count deta hai. Bohot useful hai quick overview ke liye:

df['websites'].isnull().sum()
        #  Sirf ek specific column (websites) ki missing count.        


# 2️⃣ Missing rows ko dekhna

df[df['websites'].isnull()]


# Agar sirf name aur city dekhne hain un rows ke:
df[df['websites'] .isnull()][['name', 'city']]




# 3️⃣ Missing values ko handle karna — 3 tareeqe

# Tareeqa A — Drop karna (rows hata dena):
df.dropna(subset=['websites'], inplace=True)  # websites column mein jo rows missing hain, unko hata do. inplace=True ka matlab hai original DataFrame ko modify karna.

# Tareeqa B — Fill karna (kisi value se replace karna):
df['websites'].fillna('No Website', inplace=True)  # Missing values ko 'No Website' se replace kar do.


# Tareeqa C — Poori row drop karna agar kahin bhi NaN ho:

df.dropna(inplace=True)  # Agar kisi bhi column mein NaN hai, toh poori row hata do. Ye bohot strict hai, so use carefully.

# check karna ka liya ka ab koi missing values hain ya nahi:
df.isnull().sum()  # Ab check karo, ideally sab 0 aana chahiye.



# 1. Sorting — data ko order mein lagana:

df.sort_values('name', ascending=True, inplace=True)  # name column ke hisaab se ascending order mein sort kar do. inplace=True ka matlab hai original DataFrame ko modify karna.
df.sort_values('name', ascending=False, inplace=True)  # name column ke hisaab se descending order mein sort kar do. inplace=True ka matlab hai original DataFrame ko modify karna.
df.sort_values(['city', 'name'], ascending=[True, True])#  # Pehle city ke hisaab se sort karo, phir name ke hisaab se. ascending=[True, True] ka matlab hai dono columns ke liye ascending order.  

# 2. Groupby — data ko categories mein group karke summary nikalna:

df.groupby('city').size()  # Har city mein kitne restaurants hain, unka count nikal do. Ye ek Series return karega jisme index city aur values count hongi.
df.groupby('city')['name'].count()  # Har city mein kitne restaurants hain, unka count nikal do. Ye ek Series return karega jisme index city aur values count hongi.
df.groupby('city')['name'].nunique()  # Har city mein unique restaurant names ka



# 3. Multiple columns ke sath groupby:

df.groupby(['city', 'name']).size()  #  har city mein har restaurant kitni baar aaya


# Task 2: har city mein kitne restaurants
city_counts = df.groupby('city')['name'].count()
print(city_counts)

# Task 3: sabse zyada restaurants kis city mein
city_counts.sort_values(ascending=False) 



city_counts.idxmax()   # sirf city ka naam return karega jiski count sabse zyada hai
city_counts.max()      # sirf woh maximum number return karega




# 1. .agg() — ek sath multiple statistics nikalna:

df.groupby('city')['name'].agg(['count', 'nunique'])  # Har city mein kitne restaurants hain aur unique restaurant names ka count nikal do. Ye ek DataFrame return karega jisme index city aur columns count aur unique honge.



# Multiple columns pe alag-alag functions bhi laga sakte hain:
df.groupby('city').agg({
        'name': 'count',
        'latitude': 'mean'
})


# 2. pivot_table() — Excel jaisi pivot table banana:


df.pivot_table(index='city', values= 'name', aggfunc='count')  # Har city mein kitne restaurants hain, unka count nikal do. Ye ek DataFrame return karega jisme index city aur values count hongi.




# 3. Reset index — groupby ke baad DataFrame wapis normal banana:
city_counts = df.groupby('city')['name'].count().reset_index()


# 1. Case badalna:
df['city'].str.lower()      # sab lowercase
df['city'].str.upper()      # sab UPPERCASE
df['city'].str.title()      # Har Lafz Ka Pehla Letter Capital

# 2. Extra spaces hatana:
df['city'].str.strip()      # Sirf start aur end ke extra spaces hatana

# 3. Kisi text ko dhoondna (contains):
df[df['name'].str.contains('Pizza')]
df[df['name'].str.contains('pizza',case=False)]  # case insensitive search

# 4. Replace karna:
df['name'].str.replace("McDonald's", 'McDonalds')  # McDonald's ko McDonalds se replace kar do. regex=False ka matlab hai exact match replace karna.

# 5. Split karna:

df['address'].str.split(' ')  # address ko space ke hisaab se split kar do. Ye ek list return karega har row ke liye.

# 6. Length nikalna:
df['name'].str.len()     #har naam mein kitne characters hain









# 1. city ko lowercase karke naya column banayein
df['city_clean'] = df['city'].str.lower()

# 2. kitne unique cities hain (lowercase karne ke baad)
print(df['city_clean'].nunique())

# 3. jin names mein 'Pizza' word ho (case-insensitive)
pizza_places = df[df['name'].str.contains('pizza', case=False, na=False)]
print(pizza_places.shape[0])   # total count
print(pizza_places['name'].value_counts())   




# Dominos ke sab variations ko ek jaisa banana
df['name_clean'] = df['name'].str.replace("'", "", regex=False)
df['name_clean'] = df['name_clean'].str.replace("’", "", regex=False)  
df[df['name_clean'].str.contains('Dominos Pizza', case=False, na=False)]['name_clean'].value_counts()



customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Zain']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer_id': [1, 2, 5],   
    'amount': [500, 300, 700]
})


pd.merge(customers, orders, on='customer_id', how='inner')



pd.merge(customers, orders, on='customer_id', how='left')

# Right join — right table ki saari rows:
pd.merge(customers, orders, on='customer_id', how='right')

# Outer join — dono ki saari rows, jo match na ho wahan NaN:
pd.merge(customers, orders, on='customer_id', how='outer')



# Step 9: Date/Time Operations

import pandas as pd

sales = pd.DataFrame({
    'date': ['2024-01-05', '2024-02-14', '2024-03-21', '2024-06-10'],
    'amount': [500, 300, 700, 450]
})

# 1️⃣ Text ko datetime mein convert karna (sabse zaroori step)


sales['date'] = pd.to_datetime(sales['date'])   
print(sales.dtypes)    # convert karne se pehle 'object', baad mein 'datetime64'

sales['year'] = sales['date'].dt.year
sales['month'] = sales['date'].dt.month
sales['day'] = sales['date'].dt.day
sales['weekday'] = sales['date'].dt.day_name()
print(sales)






pd.date_range('2024-01-01', periods=5, freq='D')    # 5 din, roz ek
pd.date_range('2024-01-01', periods=3, freq='M')     # 3 mahine
print(pd.date_range('2024-01-01', periods=3, freq='M'))    # 3 mahine ka range print karna

sales[sales['date'] > '2024-03-01']    # 1st Feb ke baad ki sales
sales[sales['date'].dt.month == 2]    # February ki sales

sales['days-ago'] = (pd.Timestamp('2024-12-31')-sales['date']).dt.days
print(sales)


print(df.columns.tolist())


df['category'] = df['name'].apply(classify)
print(df['category'].value_counts())


# 1. Duplicates dhoondna:
df.duplicated()          # True/False — har row batata hai duplicate hai ya nahi
df.duplicated().sum()     # kitni total duplicate rows hain

# 2. Specific columns ke hisaab se duplicates check karna:
df.duplicated(subset=['name', 'city'])   # sirf name+city match hone par duplicate mana jayega


# 3. Duplicates hatana:
df.drop_duplicates()                       # poori row same ho to hatao
df.drop_duplicates(subset=['name'])         # sirf 'name' match ho to hatao (pehli wali rakhega)
df.drop_duplicates(subset=['name'], keep='last')   # aakhri wali rakhega, pehli hatao

# Step 12: Reshaping Data — pivot() aur melt()

sales = pd.DataFrame({
    'city': ['Lahore', 'Lahore', 'Karachi', 'Karachi'],
    'year': [2023, 2024, 2023, 2024],
    'amount': [500, 600, 300, 400]
})

wide = sales.pivot(index='city', columns='year', values='amount')
print(wide)


long = wide.reset_index().melt(id_vars='city', var_name='year', value_name='amount')
print(long)


df.pivot_table(index='city', columns='country', values='name', aggfunc='count')

# Step 13: Statistics & Correlation


df['price'].mean()      # average
df['price'].median()     # middle value
df['price'].mode()        # sabse zyada baar aane wali value
df['price'].std()          # standard deviation (data kitna phela hua hai)
df['price'].var()           # variance
df['price'].min()            # minimum
df['price'].max()             # maximum
df['price'].sum()              # total




df[['bed', 'bath', 'price']].corr() 


df['city'].value_counts()                  # counts
df['city'].value_counts(normalize=True)     # percentage (0 se 1 ke darmiyan)
df['city'].value_counts().head(5)            # top 5


df['city'].describe()





































# df = pd.DataFrame({
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'marks': [85, 90, 78],
#     'subject': ['Math', 'Science', 'English']
# })


