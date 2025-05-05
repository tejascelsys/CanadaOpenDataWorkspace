# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7f1725d4-0f8a-4754-83b1-dc426503e2ce",
# META       "default_lakehouse_name": "CensusProfile",
# META       "default_lakehouse_workspace_id": "a0923a92-f29f-42fe-8cb8-9a0acd1a040a"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Import Census Profile, 2021 Census of Population - Census Profile, 2021 - Canada, Provinces and Territories
# From https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/getFile.cfm?LANG=E&GEONO=001&FILETYPE=CSV

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

# MARKDOWN ********************

# ## Unzip the file

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

# MARKDOWN ********************

# # Update the encoding

# CELL ********************

import pandas as pd
import chardet

# Path to the CSV file
csv_file_path = extract_to_path + "/98-401-X2021001_English_CSV_data.csv"

# Detect the file encoding
with open(csv_file_path, "rb") as file:
    result = chardet.detect(file.read(10000))  # Analyze the first 10KB
    detected_encoding = result['encoding']
    print(f"Detected encoding: {detected_encoding}")

# Read the file with the detected encoding
try:
    with open(csv_file_path, "r", encoding=detected_encoding, errors="replace") as f:
        df = pd.read_csv(f)
    print("File loaded successfully.")
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")
    print("Trying with 'latin1' as fallback encoding.")
    # Fallback to a common encoding if detection fails
    with open(csv_file_path, "r", encoding="latin1", errors="replace") as f:
        df = pd.read_csv(f)
        
# Display the first rows of the DataFrame
print(df.head())

# Save the DataFrame to UTF-8 for future use
utf8_file_path = csv_file_path + ".csv"
df.to_csv(utf8_file_path, index=False, encoding="utf-8")
print(f"File saved as UTF-8 at: {utf8_file_path}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Moving the CSV data to the data lake

# CELL ********************

import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.getOrCreate()

# Read the CSV into a Pandas DataFrame
csv_file_path = "/lakehouse/default/Files/98-401-X2021001_eng_CSV/98-401-X2021001_English_CSV_data.csv.csv"
df = pd.read_csv(csv_file_path)

# Convert Pandas DataFrame to Spark DataFrame
spark_df = spark.createDataFrame(df)

# Write Spark DataFrame to Data Warehouse
spark_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("2021_population")

print("Data loaded into the Data Lake.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
