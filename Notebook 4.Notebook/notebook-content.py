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

# CELL ********************

lakehouse_path = "abfss://CanadaOpenDataWorkSpace@onelake.dfs.fabric.microsoft.com/MunicipalFinancialDataLH.Lakehouse/Tables/mf_a1_total"
table_df = spark.read.format("delta").load(lakehouse_path)
cleaned_df = table_df.na.drop()
cleaned_df = table_df.select("YEAR","CODE","Total_Liabilities","Total_Non-Financial_Assets")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
df = df.toPandas()
df.head()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ##### Train a machine learning model

# CELL ********************

from sklearn.model_selection import train_test_split
    
X, y = df[['YEAR','CODE','Total_Liabilities']].values, df['Total_Non-Financial_Assets'].values

    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import mlflow
experiment_name = "experiment-MunicipalData"
mlflow.set_experiment(experiment_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from sklearn.linear_model import LinearRegression
    
with mlflow.start_run():
   mlflow.autolog()
    
   model = LinearRegression()
   model.fit(X_train, y_train)
    
   mlflow.log_param("estimator", "LinearRegression")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
