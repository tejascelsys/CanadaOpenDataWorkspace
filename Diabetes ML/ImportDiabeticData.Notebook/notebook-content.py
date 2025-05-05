# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "2fb8eb0c-9fd0-48bb-8715-7cb58c43c1ab",
# META       "default_lakehouse_name": "DiabeticLH",
# META       "default_lakehouse_workspace_id": "a0923a92-f29f-42fe-8cb8-9a0acd1a040a"
# META     }
# META   }
# META }

# CELL ********************

import requests, os;

url = "https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/getFile.cfm?LANG=E&GEONO=001&FILETYPE=CSV"
local_path = "/lakehouse/default/Files/98-401-X2021001_eng_CSV.zip"

if not os.path.exists(local_path):
    response = requests.get(url)
    with open(local_path, "wb") as f:
        f.write(response.content)
    print(f"File downloaded and saved to {local_path}")
else:
    print(f"File already exists at {local_path}, skipping download.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import zipfile
import os

# Path to the zip file
zip_file_path = local_path

# Folder to extract the contents
extract_to_path = "/lakehouse/default/Files/98-401-X2021001_eng_CSV"

# Ensure the destination folder exists
os.makedirs(extract_to_path, exist_ok=True)

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f"File extracted to: {extract_to_path}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Define expected input features and output column
expected_features = ['AGE','SEX','BMI','BP','S1','S2','S3','S4','S5','S6']  # Replace with actual feature names
output_column = 'Y' # Replace with the actual output column name

# Ensure the DataFrame contains the required features and output column
required_columns = expected_features + [output_column]
df = df.select(required_columns)

# Cast input features and output column to float64
from pyspark.sql.types import DoubleType
for column in required_columns:
    df = df.withColumn(column, df[column].cast(DoubleType()))

# Save the cleaned table back to Lakehouse
cleaned_path = "Files/cleaned_diabetes_data"
df.write.format("parquet").mode("overwrite").save(cleaned_path)

print("Data prepared and saved at: " + cleaned_path)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Load the Parquet file from the Lakehouse
lakehouse_parquet_path = "Files/cleaned_diabetes_data"
df_from_parquet = spark.read.format("parquet").load(lakehouse_parquet_path)

# Define Delta table path in the Lakehouse
delta_table_path = "Tables/cleaned_diabetes"

# Write data as a Delta table
df_from_parquet.write.format("delta").mode("overwrite").save(delta_table_path)

print("Data saved as Delta table at: " + delta_table_path)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
