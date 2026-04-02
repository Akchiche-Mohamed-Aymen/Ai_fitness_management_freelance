from pandas import read_csv, to_numeric

df = read_csv("weightlifting_cleaned.csv")

# Ensure numeric types.
for col in ["weight", "reps", "sets"]:
    df[col] = to_numeric(df[col], errors="coerce")

    
median_volume = (df["weight"] * df["reps"] * df["sets"]).median()
def generate_success(row):
    volume = row["weight"] * row["reps"] * row["sets"]
    return 1 if volume >= median_volume else 0
df["success"] = df.apply(generate_success, axis=1)
df.to_csv("weightlifting_cleaned.csv", index=False)
# py add_success_labels.py
