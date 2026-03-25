from pandas import read_csv, to_numeric

df = read_csv("weightlifting_cleaned.csv")

# Ensure numeric types.
for col in ["weight", "reps", "sets"]:
    df[col] = to_numeric(df[col], errors="coerce")
if "rpe" in df.columns:
    df["rpe"] = to_numeric(df["rpe"], errors="coerce")

# Rule-based success using only this file:
# baseline reps = median reps for similar load/sets pattern.
df["expected_reps"] = df.groupby(["weight", "sets"], dropna=False)["reps"].transform("median")

df["success"] = (df["reps"] >= (df["expected_reps"])).astype(int)


df["success"] = df["success"].astype(int)
df.drop(columns=["expected_reps"], inplace=True)
df.to_csv("weightlifting_cleaned.csv", index=False)

print(df["success"].value_counts())
# py add_success_labels.py
