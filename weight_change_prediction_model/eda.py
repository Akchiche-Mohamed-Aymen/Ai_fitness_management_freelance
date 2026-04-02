import pandas as pd
from pandas import read_csv

df = read_csv('weightlifting_cleaned.csv')
# Investigate weight column for anomalies
print("\nWeight column investigation:")
print(f"Min weight: {df.weight.min()}")
print(f"Max weight: {df.weight.max()}")
print(f"Unique weights : {len(df.weight.unique())} rows")
print(f"Number of not allowed weights: {(df.weight < 40).sum()}")
# Weight distribution
bins = [0, 10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
cut= pd.cut(df['weight'], bins=bins)
print("\nWeight distribution by bins:")
print(cut.value_counts().sort_index())
# Clean the data: remove weight == 0 and weight > 500
df = df[df['weight'] >= 40]
print(f"\nAfter cleaning: {df.shape[0]} rows (removed {df.shape[0] - df.shape[0]})")
print(f"Cleaned weight stats: min={df.weight.min():.2f}, max={df.weight.max():.2f}, variance={df.weight.var():.2f}")
# Filter out rows with reps outside 3-15 range
df = df[(df.reps >= 3) & (df.reps <= 15)]
#length of sets 3 <= sets <= 8
df = df[(df.sets >= 1) & (df.sets <= 8)]
# Save cleaned data
df.to_csv('weightlifting_cleaned.csv', index=False)
print("Saved cleaned data to weightlifting_cleaned.csv")

#cls ; py eda.py
