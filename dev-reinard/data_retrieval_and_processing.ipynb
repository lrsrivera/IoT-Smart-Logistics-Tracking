total_records = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_records}")

import pandas as pd


# Retrieve all IoT records
data = []
for i in range(total_records):
    record = contract.functions.getRecord(i).call()
    data.append({
        "timestamp": record[0],
        "device_id": record[1],
        "data_type": record[2],
        "data_value": record[3]
    })


# Convert to a DataFrame
df = pd.DataFrame(data)


# Convert timestamp to readable format
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")


# Display first few records
print(df.head())

import numpy as np


# Extract numeric values from 'data_value' where applicable
df["numeric_value"] = df["data_value"].str.extract(r'(\d+\.?\d*)').astype(float)


# Handle missing values (if any)
df.fillna(0, inplace=True)


# Display cleaned data
print(df.head())

# Save cleaned IoT data to a CSV file
df.to_csv("cleaned_iot_data.csv", index=False)


print("✅ Cleaned IoT data saved successfully as cleaned_iot_data.csv")
