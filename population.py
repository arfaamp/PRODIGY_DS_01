import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "india_statewise_population_with_all_india.csv"  # Ensure correct file path
df = pd.read_csv(file_path)

# Strip column names to avoid hidden spaces
df.columns = df.columns.str.strip()

# Print available columns to verify column names
print("Available Columns:", df.columns)

# Define states and verify age group column names
states = df["State"]

# Replace with the actual column names from your dataset
age_groups = [col for col in df.columns if col not in ["State", "Total Population"]]

# Set figure size
plt.figure(figsize=(14, 7))

# Define positions for grouped bars
x = np.arange(len(states))  # X-axis positions for states
width = 0.1  # Bar width

# Plot bars for each age group
for i, age_group in enumerate(age_groups):
    plt.bar(x + i * width, df[age_group], width, label=age_group)

# Labeling
plt.xlabel("States")
plt.ylabel("Population Count")
plt.title("Age-wise Distribution Across States")
plt.xticks(x + width * (len(age_groups) / 2), states, rotation=90)  # Adjust X-axis labels
plt.legend(title="Age Groups", bbox_to_anchor=(1.05, 1), loc="upper left")

# Show plot
plt.tight_layout()
plt.show()
