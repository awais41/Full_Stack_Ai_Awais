import pandas as pd 
df = pd.read_csv('diamonds.csv')

x = df['carat'].values.reshape(-1, 1)
y = df['price'].values.reshape(-1, 1)

df.plot.scatter(x='carat', y='price', title='Carat vs Price of Diamonds')
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)
input('wait for me .....................')
