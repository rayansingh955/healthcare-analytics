import pandas as pd
import numpy as np

df = pd.read_csv("healthcare_dataset.csv")

# Remove duplicates
df = df.drop_duplicates()

# Create age group
bins = [0, 30, 45, 60, 100]
labels = ["Young", "Middle", "Senior", "Elderly"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

# Create risk level
df["RiskLevel"] = np.where(df["HighRisk"] == 1, "High", "Low")

# Save cleaned data
df.to_csv("cleaned_healthcare_data.csv", index=False)

print("Data cleaned successfully")
