# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "359e1de8-074c-47ce-a2ca-37643bdaa1ce",
# META       "default_lakehouse_name": "Catalogue",
# META       "default_lakehouse_workspace_id": "0e74681b-43b8-4256-bbfb-79b38578b805",
# META       "known_lakehouses": [
# META         {
# META           "id": "640bc3e2-4d27-4a1c-a669-20bee8c08945"
# META         },
# META         {
# META           "id": "359e1de8-074c-47ce-a2ca-37643bdaa1ce"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "default_warehouse": "5de4d395-6d74-a9e0-4347-89c2de169c6b",
# META       "known_warehouses": [
# META         {
# META           "id": "5de4d395-6d74-a9e0-4347-89c2de169c6b",
# META           "type": "Datawarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Download the **Open Data Portal Catalogue - Catalogue** 
# 
# from https://open.canada.ca/data/dataset/c4c5c7f1-bfa6-4ff6-b4a0-c164cb2060f7/resource/b8931c16-0710-4c31-bbda-f60841e98cb4

# CELL ********************

import requests, os;

url = "https://open.canada.ca/data/dataset/c4c5c7f1-bfa6-4ff6-b4a0-c164cb2060f7/resource/b8931c16-0710-4c31-bbda-f60841e98cb4/download/output.xlsx"
local_path = "/lakehouse/default/Files/OpenDataPortalCatalogue.xlsx"

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

# # From OpenDataPortalCatalogue.xlsx to Lake Tables

# CELL ********************

import pandas as pd
from pyspark.sql import SparkSession


# Initialize SparkSession
spark = SparkSession.builder.appName("FabricExcelImport").getOrCreate()

# Read the Excel file with pandas to get all sheets
excel_data = pd.ExcelFile(local_path)

# Iterate through each sheet in the Excel file
for sheet_name in excel_data.sheet_names:
    # Load the data from the current sheet into a pandas DataFrame
    sheet_df = excel_data.parse(sheet_name)
    
    # Convert the pandas DataFrame to a Spark DataFrame
    spark_df = spark.createDataFrame(sheet_df)
    
    # Define the target table name
    table_name = f"Catalogue_{sheet_name}"
    
    # Drop the table if it exists
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")
    
    # Write the data to a new table
    spark_df.write.mode("overwrite").saveAsTable(table_name)
    
    print(f"Table '{table_name}' created and data imported.")

print("All sheets have been processed and imported into Fabric.")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # From Lake to Warehouse
