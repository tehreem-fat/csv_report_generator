import pandas as pd
import matplotlib.pyplot as plt
import os

# Create reports directory if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Load CSV file
data_file = "data/sample_data.csv"
df = pd.read_csv(data_file)

# Display basic info
print("Data Head:\n", df.head())
print("\nData Description:\n", df.describe())

# Generate summary statistics
summary = df.describe()
summary.to_excel("reports/summary_report.xlsx")
print("\nSummary report saved to reports/summary_report.xlsx")

# Generate charts
plt.figure(figsize=(8,6))
if "Sales" in df.columns:
    df['Sales'].plot(kind='bar', title='Sales Bar Chart')
    plt.savefig("reports/sales_chart.png")
    print("Sales chart saved to reports/sales_chart.png")

plt.show()
