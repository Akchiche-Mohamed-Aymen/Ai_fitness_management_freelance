from pandas import read_csv

f1, f2 = "workouts.csv", "weightlifting_workouts.csv"
df1 = read_csv(f1)
df2 = read_csv(f2)

df2 = df2[df2["Exercise Name"] != "Lateral Raise (Dumbbell)"]

# One block = same workout instant + workout name + exercise (sets belong together).
SESSION_KEYS = ["Date", "Workout Name", "Exercise Name"]
df2 = df2.sort_values(
    SESSION_KEYS + ["Set Order"], kind="mergesort"
).reset_index(drop=True)

df2["sets"] = df2.groupby(SESSION_KEYS, sort=False)["Set Order"].transform("max")
df2["Weight"] = df2["Weight"] * 0.45359237

df2.rename(columns={"Weight": "weight", "Reps": "reps", "sets": "sets"}, inplace=True)

# Rule-based success (0/1) for weightlifting rows only — uses within-exercise set order.
# - First set in the block: success = 1
# - Load changed vs previous set (heavier or lighter): success = 1 (new target)
# - Same load: success = 1 if reps did not drop by more than 1 vs previous set
w_prev = df2.groupby(SESSION_KEYS, sort=False)["weight"].shift(1)
r_prev = df2.groupby(SESSION_KEYS, sort=False)["reps"].shift(1)
is_first = df2.groupby(SESSION_KEYS, sort=False).cumcount() == 0
same_weight = df2["weight"] == w_prev
reps_ok = df2["reps"] >= (r_prev - 1)
load_changed = df2["weight"] != w_prev
df2["success"] = (
    is_first | load_changed | (same_weight & reps_ok)
).astype(int)

df1.rename(columns={"weight_kg": "weight"}, inplace=True)
df1 = df1[["weight", "reps", "rpe"]]
df2 = df2[["weight", "reps", "sets", "success"]]

df1.to_csv("workouts_cleaned.csv", index=False)
df2.to_csv("weightlifting_cleaned.csv", index=False)

# py prepare_workout_csvs.py
