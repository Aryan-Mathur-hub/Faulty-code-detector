import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import os
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

# Load the dataset
file_path = "Datasets/jm1.csv" #Or kc1.csv
df = pd.read_csv(file_path)

# Convert object columns to numeric
numeric_cols = ["uniq_Op", "uniq_Opnd", "total_Op", "total_Opnd", "branchCount"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Fill missing values with median
df.fillna(df.median(numeric_only=True), inplace=True)

# Split features and target
X = df.drop(columns=["defects"])
y = df["defects"].astype(int)  # Convert boolean to int (0,1)

# Handle class imbalance using SMOTE
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Convert resampled data back to a DataFrame
processed_df = pd.DataFrame(X_resampled, columns=X.columns)
processed_df["defects"] = y_resampled  # Add the target column back

# Save to CSV
processed_df.to_csv("Datasets/processed_jm1.csv", index=False)   #For kc1.csv, use "processed_kc1.csv"

print("Processed dataset saved as 'processed_jm1.csv'. Ready for model training!")  # For kc1.csv, use "processed_kc1.csv"