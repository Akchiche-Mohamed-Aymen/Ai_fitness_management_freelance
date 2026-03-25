from pandas import DataFrame, read_csv, to_numeric
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def clean_column(df: DataFrame, column: str) -> DataFrame:
    df[column] = to_numeric(df[column], errors="coerce")
    skew = abs(df[column].skew())
    if skew > 1:
        df.fillna({column: df[column].median()}, inplace=True)
    else:
        df.fillna({column: df[column].mean()}, inplace=True)
    return df


def evaluate(y_true, y_pred):
    rmse = (mean_squared_error(y_true, y_pred) ** 0.5)
    mae = mean_absolute_error(y_true, y_pred)
    return rmse, mae


df1 = read_csv("workouts_cleaned.csv")
df2 = read_csv("weightlifting_cleaned.csv")

# Handle missing values and ensure numeric columns.
for col in ["weight", "reps", "rpe"]:
    df1 = clean_column(df1, col)
for col in ["weight", "reps"]:
    df2 = clean_column(df2, col)

if "success" in df2.columns:
    df2["success"] = to_numeric(df2["success"], errors="coerce").fillna(0).clip(0, 1).astype(int)

df1["reps"] = df1["reps"].round().astype(int)
df2["reps"] = df2["reps"].round().astype(int)

X = df1[["weight", "reps"]]
y = df1["rpe"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.001, max_iter=10000),
    "RandomForest": RandomForestRegressor(
        n_estimators=300, random_state=42, min_samples_leaf=2
    ),
    "GradientBoosting": GradientBoostingRegressor(random_state=42),
    "KNN": Pipeline(
        [("scaler", StandardScaler()), ("model", KNeighborsRegressor(n_neighbors=7))]
    ),
}

results = []
fitted_models = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse, mae = evaluate(y_test, y_pred)
    results.append((model_name, rmse, mae))
    fitted_models[model_name] = model

# Lower MAE is primary target for RPE prediction quality.
results.sort(key=lambda x: x[2])

print("Model leaderboard (sorted by MAE):")
for rank, (name, rmse, mae) in enumerate(results, start=1):
    print(f"{rank:>2}. {name:<18} RMSE={rmse:.3f} MAE={mae:.3f}")

best_name, best_rmse, best_mae = results[0]
best_model = fitted_models[best_name]

print("\nBest model selected:")
print(f"{best_name}  |  RMSE={best_rmse:.3f}  MAE={best_mae:.3f}")

# Train best model on full df1 then infer missing rpe for df2.
best_model.fit(X, y)
df2["rpe"] = best_model.predict(df2[["weight", "reps"]]).clip(1, 10).round(2)
df2.to_csv("weightlifting_cleaned.csv", index=False)
print("Saved predictions to weightlifting_cleaned.csv")

# py predict_rpe.py
