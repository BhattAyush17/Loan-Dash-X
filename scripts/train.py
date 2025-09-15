import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load data
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'loan_data.csv')
df = pd.read_csv(DATA_PATH)

# Features and target
X = df[["income", "credit_score", "loans_ongoing", "age", "gender"]]
y = df["loan_approved"]

# Preprocessing
numeric_features = ["income", "credit_score", "loans_ongoing", "age"]
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])
categorical_features = ["gender"]
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])
preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# Model pipeline
clf = RandomForestClassifier(random_state=42)
pipe = Pipeline([
    ("pre", preprocessor),
    ("clf", clf)
])

# Hyperparameter tuning (small grid for demo purpose)
param_grid = {"clf__n_estimators": [100, 200]}
grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
grid.fit(X, y)

# Save model to models/ folder
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'loan_approval_pipeline.joblib')
joblib.dump(grid.best_estimator_, MODEL_PATH)
print(f"Model saved to: {MODEL_PATH}")