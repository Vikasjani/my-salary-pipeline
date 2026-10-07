import pandas as pd
import numpy as np

print("--- Employee Salary Processing Data Pipeline ---")
# Corrected Sample data generation
data = {
    'Employee_ID': [101, 102, 103, 104],
    'Experience_Years': [2, 5, 8, 1],
    'Base_Salary': [50000, 75000, 95000, 45000]
}
df = pd.DataFrame(data)

# Pipeline transformation: Adding 10% bonus based on experience
df['Bonus'] = np.where(df['Experience_Years'] > 3, df['Base_Salary'] * 0.10, df['Base_Salary'] * 0.05)
df['Total_Salary'] = df['Base_Salary'] + df['Bonus']

print("\nPipeline executed successfully! Cleaned Salary Data:")
print(df.to_string(index=False))
