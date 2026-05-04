import pandas as pd
from data_profiling import ProfileReport

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Generate report
profile = ProfileReport(df, title="EDA Report")

# Save report
profile.to_file("report.html")

print("Report generated successfully!")
