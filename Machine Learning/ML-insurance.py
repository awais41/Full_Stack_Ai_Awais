import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

# 1. Load data
df = pd.read_csv("insurance.csv")

# 2. Clean data
df = df.drop_duplicates()

# 3. Feature engineering
df["is_obese"] = (df["bmi"] >= 30).astype(int)
df["smoker_obese"] = ((df["smoker"] == "yes") & (df["is_obese"] == 1)).astype(int)

# 4. Split features and target
X = df.drop("charges", axis=1)
y = df["charges"]

# 5. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Preprocessing (scale numbers, encode categories)
numeric_features = ["age", "bmi", "children", "is_obese", "smoker_obese"]
categorical_features = ["sex", "smoker", "region"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(drop="first"), categorical_features),
])

# 7. Model (best params we found earlier)
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=2, random_state=42)),
])

# 8. Train
model.fit(X_train, y_train)

# 9. Evaluate
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Train R2:", r2_score(y_train, train_pred))
print("Test R2:", r2_score(y_test, test_pred))
print("Test MAE:", mean_absolute_error(y_test, test_pred))
print("Test RMSE:", np.sqrt(mean_squared_error(y_test, test_pred)))

# 10. Save model
joblib.dump(model, "insurance_model.pkl")
print("Model saved as insurance_model.pkl")