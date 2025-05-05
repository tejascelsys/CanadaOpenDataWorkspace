# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "78c29da6-83f6-4fff-8e53-01ba548fd5e2",
# META       "default_lakehouse_name": "MunicipalFinancialDataLH",
# META       "default_lakehouse_workspace_id": "a0923a92-f29f-42fe-8cb8-9a0acd1a040a",
# META       "known_lakehouses": [
# META         {
# META           "id": "78c29da6-83f6-4fff-8e53-01ba548fd5e2"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## Download The File And Save Into Lake House Files Section

# CELL ********************

import requests, os;

url = "https://open.alberta.ca/dataset/cde4c4fd-a0b2-4816-af43-13de7a3fd3e3/resource/78ee285e-460a-44d9-898a-a50b30bb1341/download/2023_financial_year.xlsx"
local_path = "/lakehouse/default/Files/2023FinancialYear.xlsx"

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

# ## Read the XLS File and Load Into Delta Table Of Lake House

# CELL ********************

import pandas as pd
from pyspark.sql import SparkSession

local_path = "/lakehouse/default/Files/2023FinancialYear.xlsx"

# Specify the sheet to skip and the rows to exclude
sheet_to_skip = "Index"  # Replace with the actual sheet name you want to skip
rows_to_skip = [0, 2]  # Replace with the 0-based row indices you want to skip

# Initialize SparkSession
spark = SparkSession.builder.appName("MunicipalFinancialDataExcelImportIntoOnelake").getOrCreate()

# Read the Excel file with pandas to get all sheets
excel_data = pd.ExcelFile(local_path)

# Iterate through each sheet in the Excel file
for sheet_name in excel_data.sheet_names:
    # Skip the specified sheet
    if sheet_name == sheet_to_skip:
        print(f"Skipping sheet: {sheet_name}")
        continue

    # Load the data from the current sheet into a pandas DataFrame, skipping specified rows
    sheet_df = excel_data.parse(sheet_name, skiprows=rows_to_skip)

    # Remove spaces and commas from column names
    sheet_df.columns = [col.replace(" ", "_").replace(",", "").replace("(", "").replace(")", "") for col in sheet_df.columns]
    
    # Replace invalid characters in the table name
    sanitized_sheet_name = sheet_name.replace("(", "").replace(")", "").replace("-", "_").replace(" ", "_")
    table_name = f"mf_{sanitized_sheet_name}"
    
    # Drop the table if it exists
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")
    
    # Write the data to a new table
    spark_df = spark.createDataFrame(sheet_df)
    spark_df.write.mode("overwrite").saveAsTable(table_name)
    
    print(f"Table '{table_name}' created and data imported.")

print("All sheets have been processed and imported into MuniciapalFinancialData Lake House, excluding the specified sheet.")


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
