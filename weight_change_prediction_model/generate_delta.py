from pandas import read_csv

# load dataset
f1  = "weightlifting_cleaned.csv"
data = read_csv(f1)

# define rule-based delta generator
def next_weight_delta(row):
    success = row["success"]
    reps = row["reps"]
    sets = row["sets"]

    # success cases
    if success == 1:
        if reps >= 8 and sets >= 6:
            return 5
        elif reps >= 6:
            return 2.5
        else:
            return 0

    # failure cases
    else:
        if reps >= 6:
            return -2.5
        else:
            return -5


data["delta_weight"] = data.apply(next_weight_delta, axis=1)

# save updated dataset
data.to_csv(f1, index=False)

print("delta_weight column added successfully")
#py generate_delta.py