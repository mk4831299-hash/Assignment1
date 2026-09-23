import pandas as pd

# Create DataFrame
data = {
    "Student Name": ["Amit", "Riya", "Sourav", "Neha", "Rahul"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [72, 85, 68, 91, 77],
    "Attendance": [88, 92, 76, 95, 81]
}

df = pd.DataFrame(data)

print("--- Complete DataFrame ---")
print(df)

# Filter students who scored above 80
filtered_df = df[df["Marks"] > 80]

print("\n--- Students Scoring Above 80 ---")
print(filtered_df)