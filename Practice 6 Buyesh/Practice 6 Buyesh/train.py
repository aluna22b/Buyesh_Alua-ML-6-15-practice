import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load dataset
df = pd.read_csv("job_salary_prediction_dataset.csv")

# 2. Target column
target_column = "salary"

# 3. Check target
if target_column not in df.columns:
    raise ValueError(
        f"Column '{target_column}' was not found. Available columns: {list(df.columns)}"
    )

# 4. Keep only needed columns
feature_columns = [
    "experience_years",
    "skills_count",
    "certifications",
    "job_title",
    "education_level",
    "industry",
    "company_size",
    "location",
    "remote_work"
]

required_columns = feature_columns + [target_column]

missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Missing columns in dataset: {missing_columns}")

df = df[required_columns].copy()

# 5. Convert target to numeric if needed
df[target_column] = (
    df[target_column]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("k", "000", regex=False)
    .str.strip()
)

df[target_column] = pd.to_numeric(df[target_column], errors="coerce")

# 6. Drop rows where target is missing
df = df.dropna(subset=[target_column])

# 7. Split features and target
X = df[feature_columns]
y = df[target_column]

# 8. Define numeric and categorical columns
numeric_features = [
    "experience_years",
    "skills_count",
    "certifications"
]

categorical_features = [
    "job_title",
    "education_level",
    "industry",
    "company_size",
    "location",
    "remote_work"
]

print("Numeric columns:", numeric_features)
print("Categorical columns:", categorical_features)

# 9. Preprocessing for numeric columns
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

# 10. Preprocessing for categorical columns
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# 11. Combine preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# 12. Create full pipeline

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=20,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    ))
])

# 13. Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 14. Train model
print("Start training...")
model.fit(X_train, y_train)
print("Training finished!")

# 15. Predict
print("Start prediction...")
y_pred = model.predict(X_test)
print("Prediction finished!")

# 16. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.2f}")
print(f"R2: {r2:.4f}")

# 17. Save model and feature names
joblib.dump(model, "model.joblib")
joblib.dump(feature_columns, "model_features.joblib")

print("Model saved as model.joblib")
print("Feature list saved as model_features.joblib")