# Step 11: Cross-validate the final model properly

import pandas as pd
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

df = pd.read_csv('Bank.csv')  # your path
df['was_contacted_before'] = (df['pdays'] != -1).astype(int)
df['deposit'] = df['deposit'].map({'yes': 1, 'no': 0})

cat_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

X = df_encoded.drop('deposit', axis=1)
y = df_encoded['deposit']

# StratifiedKFold keeps the yes/no ratio consistent in every fold
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf_scores = cross_val_score(rf, X, y, cv=cv, scoring='accuracy')

# XGBoost (tuned params from Step 8)
xgb = XGBClassifier(n_estimators=200, max_depth=7, learning_rate=0.05,
                     random_state=42, eval_metric='logloss')
xgb_scores = cross_val_score(xgb, X, y, cv=cv, scoring='accuracy')

print("Random Forest -- 5-fold CV scores:", rf_scores)
print(f"Random Forest -- Mean: {rf_scores.mean():.4f}  Std: {rf_scores.std():.4f}")
print()
print("XGBoost -- 5-fold CV scores:", xgb_scores)
print(f"XGBoost -- Mean: {xgb_scores.mean():.4f}  Std: {xgb_scores.std():.4f}")