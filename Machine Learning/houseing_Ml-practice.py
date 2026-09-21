import pandas as pd 
df = pd.read_csv('housing.csv')
print(df.head())

print(df.shape)
df.info()
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
print(df["ocean_proximity"].value_counts())
print(df['total_bedrooms'].median())

df['total_bedrooms'] = df['total_bedrooms'].fillna(
    df['total_bedrooms'].median()
)
# Feature Engineering

df["rooms_per_household"] = (
    df["total_rooms"] / df["households"]
)

df["bedrooms_per_room"] = (
    df["total_bedrooms"] / df["total_rooms"]
)

df["population_per_household"] = (
    df["population"] / df["households"]
)

print("New features:")
print(df[
    [
        "rooms_per_household",
        "bedrooms_per_room",
        "population_per_household"
    ]
].head())

X = df.drop('median_house_value', axis=1)
y = df['median_house_value']

print(X.head())
print(y.head())
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(X[['ocean_proximity']])

print(encoded[:5])
print(encoder.categories_)

# Remove categorical column
X = X.drop('ocean_proximity', axis=1)

# Add encoded columns
X[['ocean_1', 'ocean_2', 'ocean_3', 'ocean_4', 'ocean_5']] = encoded

print(X.head())
print(X.shape)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled[:5])
print(X_test_scaled[:5])

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train_scaled, y_train)

print("Model trained successfully!")

# Prediction
y_pred = model.predict(X_test_scaled)

print("Predicted prices:")
print(y_pred[:5])

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

from sklearn.tree import DecisionTreeRegressor

tree_model = DecisionTreeRegressor(random_state=42)

tree_model.fit(X_train_scaled, y_train)

tree_pred = tree_model.predict(X_test_scaled)

print("Decision Tree predictions:")
print(tree_pred[:5])

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

tree_mae = mean_absolute_error(y_test, tree_pred)
tree_mse = mean_squared_error(y_test, tree_pred)
tree_rmse = np.sqrt(tree_mse)
tree_r2 = r2_score(y_test, tree_pred)

print("Decision Tree MAE:", tree_mae)
print("Decision Tree MSE:", tree_mse)
print("Decision Tree RMSE:", tree_rmse)
print("Decision Tree R2 Score:", tree_r2)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

# Define the parameter grid for RandomizedSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    "max_features": [1.0, "sqrt", "log2"]
}

# Initialize the RandomForestRegressor
rf_model = RandomForestRegressor(random_state=42)

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(
    rf_model,
    param_distributions=param_grid,
    n_iter=10,
    cv=5,
    random_state=42
)

random_search.fit(X_train_scaled, y_train)

rf_pred = random_search.predict(X_test_scaled)

print("Random Forest predictions:")
print(rf_pred[:5])

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_pred)

print("Random Forest MAE:", rf_mae)
print("Random Forest MSE:", rf_mse)
print("Random Forest RMSE:", rf_rmse)
print("Random Forest R2 Score:", rf_r2)

import joblib

joblib.dump(random_search, "random_forest_house_model.pkl")

print("Random Forest model saved successfully!")

