# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "082bf411-aae3-4cec-bab0-e1c43edb1cf0",
# META       "default_lakehouse_name": "Economic",
# META       "default_lakehouse_workspace_id": "a0923a92-f29f-42fe-8cb8-9a0acd1a040a"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Import Provincial and territorial economic accounts: Interactive tool

# CELL ********************

import requests, os

# List of URLs to download datasets
urls = [
    "https://www150.statcan.gc.ca/n1/tbl/csv/36100221-eng.zip",
    "https://www150.statcan.gc.ca/n1/tbl/csv/36100222-eng.zip"  # Add your second dataset URL here
]

# Local path template (update the filename dynamically)
local_base_path = "/lakehouse/default/Files/"

# Iterate over the URLs
for url in urls:
    # Extract the file name from the URL
    file_name = url.split("/")[-1]
    local_path = os.path.join(local_base_path, file_name)

    # Check if the file already exists
    if not os.path.exists(local_path):
        print(f"Downloading {file_name}...")
        response = requests.get(url)
        
        # Save the file locally
        if response.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(response.content)
            print(f"File downloaded and saved to {local_path}")
        else:
            print(f"Failed to download {file_name}. HTTP Status Code: {response.status_code}")
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

# List of zip file paths
zip_files = [
    "/lakehouse/default/Files/36100221-eng.zip",
    "/lakehouse/default/Files/36100222-eng.zip"  # Add the path to your second zip file
]

# Base extraction folder
base_extract_to_path = "/lakehouse/default/Files/Extracted/"

# Process each zip file
for zip_file_path in zip_files:
    # Extract the file name (without extension) to use as a folder name
    file_name = os.path.basename(zip_file_path).replace(".zip", "")
    extract_to_path = os.path.join(base_extract_to_path, file_name)
    
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

import pandas as pd
import chardet
import os

# Base folder where the files are located
base_extract_to_path = "/lakehouse/default/Files/Extracted/"

# List of relative paths to the CSV files
csv_files = [
    os.path.join(base_extract_to_path, "36100221-eng/36100221.csv"),
    os.path.join(base_extract_to_path, "36100222-eng/36100222.csv")  # Add your second CSV file path here
]
# Folder to save the re-encoded UTF-8 files
utf8_output_folder = os.path.join(base_extract_to_path, "utf8_converted")
os.makedirs(utf8_output_folder, exist_ok=True)

# Process each CSV file
for csv_file_path in csv_files:
    # Detect the file encoding
    with open(csv_file_path, "rb") as file:
        result = chardet.detect(file.read(10000))  # Analyze the first 10KB
        detected_encoding = result['encoding']
        print(f"Detected encoding for {csv_file_path}: {detected_encoding}")
    
    # Read the file with the detected encoding
    try:
        with open(csv_file_path, "r", encoding=detected_encoding, errors="replace") as f:
            df = pd.read_csv(f)
        print(f"File {csv_file_path} loaded successfully.")
    except UnicodeDecodeError as e:
        print(f"Error reading the file {csv_file_path}: {e}")
        print("Trying with 'latin1' as fallback encoding.")
        # Fallback to a common encoding if detection fails
        with open(csv_file_path, "r", encoding="latin1", errors="replace") as f:
            df = pd.read_csv(f)
    
    # Save the DataFrame to UTF-8 for future use
    utf8_file_path = os.path.join(utf8_output_folder, os.path.basename(csv_file_path))
    df.to_csv(utf8_file_path, index=False, encoding="utf-8")
    print(f"File saved as UTF-8 at: {utf8_file_path}")

print("Processing completed for all files.")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
from pyspark.sql import SparkSession
import os

# Initialize Spark Session
spark = SparkSession.builder.getOrCreate()

# Base path for files
base_path = "/lakehouse/default/Files/Extracted/utf8_converted/"

# List of file names and corresponding table names
files_and_tables = [
    ("36100221.csv", "income_based"),
    ("36100222.csv", "expenditure_based")  # Add more files and table names as needed
]

# Process each file
for file_name, table_name in files_and_tables:
    csv_file_path = os.path.join(base_path, file_name)
    
    # Read the CSV into a Pandas DataFrame
    print(f"Processing file: {csv_file_path}")
    df = pd.read_csv(csv_file_path)
    
    # Convert Pandas DataFrame to Spark DataFrame
    spark_df = spark.createDataFrame(df)
    
    # Write Spark DataFrame to Data Warehouse
    spark_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(table_name)
    
    print(f"Data loaded into the table: {table_name}")

print("All files processed successfully.")

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

# CELL ********************


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
