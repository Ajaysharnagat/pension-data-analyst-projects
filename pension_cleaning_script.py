import pandas as pd

# Load pension data
df = pd.read_csv("pension_disbursement.csv")

# Fill missing values
df['Amount'] = df['Amount'].fillna(method='ffill')

# Convert disbursement date to datetime
df['Disbursement_Date'] = pd.to_datetime(df['Disbursement_Date'])

# Flag pending transactions
df['Is_Pending'] = df['Status'].apply(lambda x: 1 if x != 'Completed' else 0)

# Group by scheme and get total disbursed amount
summary = df.groupby('Scheme')['Amount'].sum().reset_index()

# Output results
summary.to_csv("pension_summary.csv", index=False)
