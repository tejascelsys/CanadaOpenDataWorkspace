# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "9657e88e-1ed6-4a02-9357-5ebf255d9954",
# META       "default_lakehouse_name": "Real_Time_Local_Business_Index_LH",
# META       "default_lakehouse_workspace_id": "a0923a92-f29f-42fe-8cb8-9a0acd1a040a",
# META       "known_lakehouses": [
# META         {
# META           "id": "9657e88e-1ed6-4a02-9357-5ebf255d9954"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## Download The Zip file Into Lake House Files Path

# CELL ********************

# import requests, os;

# url = "https://www150.statcan.gc.ca/n1/tbl/csv/33100398-eng.zip"
# local_path = "/lakehouse/default/Files/33100398-eng.zip"

# if not os.path.exists(local_path):
#     response = requests.get(url)
#     with open(local_path, "wb") as f:
#         f.write(response.content)
#     print(f"File downloaded and saved to {local_path}")
# else:
#     print(f"File already exists at {local_path}, skipping download.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## UNZIP The File From Lake House 

# CELL ********************

import zipfile
import os

# Path to the zip file
local_path = "/lakehouse/default/Files/33100398-eng.zip"
zip_file_path = local_path  # Define your local path here

# Folder to extract the contents
extract_to_path = "/lakehouse/default/Files/33100398-eng.csv"  # Extract folder (not the file name)

# Ensure the destination folder exists
if os.path.exists(extract_to_path) and os.listdir(extract_to_path):
    print(f"ZIP file already extracted at: {extract_to_path}")
else:
    # Create the destination folder if it doesn't exist
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

# ## Read The CSV File And Load Into Delta Table Of Lake House

# CELL ********************

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Load CSV to Delta Lake") \
    .getOrCreate()

# Define paths
csv_path = "abfss://CanadaOpenDataWorkSpace@onelake.dfs.fabric.microsoft.com/Real_Time_Local_Business_Index_LH.Lakehouse/Files/33100398-eng.csv/33100398.csv"  # Path to the CSV file in the Lakehouse
delta_table_path = "Tables/Local_Business_Condition_Index"  # Path to the Delta Lake table in Fabric Lakehouse

# Read CSV data from Lakehouse
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(csv_path)

# Show the DataFrame (optional, for verification)
df.show()

# Write data to Delta Lake table
df.write.format("delta") \
    .mode("overwrite") \
    .save(delta_table_path)

print(f"Data successfully loaded to Delta table: {delta_table_path}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
