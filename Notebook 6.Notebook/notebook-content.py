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

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Load the CSV file
df = spark.read.format("csv").option("header", "true").load("/Lakehouse/Files/your_csv_file.csv")

# Show the data
df.show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

! pip install python-dotenv langchain langchain-community langchain-openai langchainhub openai tiktoken azure-ai-documentintelligence azure-identity azure-search-documents==11.6.0b3

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import os
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://cel-azure-ai-services.cognitiveservices.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "9e6d4742ab2a4f32bbbb9585291def02"
doc_intelligence_endpoint = "https://westus.api.cognitive.microsoft.com/"
doc_intelligence_key = "5c77c2ee32fa4cd3bb185d18f76ce39a"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install --upgrade langchain langchainhub langchain-openai langchain-community


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip freeze | grep langchain


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#pip install --upgrade typing-extensions
!pip install --upgrade --no-cache-dir typing-extensions


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip show typing-extensions


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from langchain import hub
# from langchain_openai import AzureChatOpenAI
# from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
# from langchain_openai import AzureOpenAIEmbeddings
# from langchain.schema import StrOutputParser
# from langchain.schema.runnable import RunnablePassthrough
# from langchain.text_splitter import MarkdownHeaderTextSplitter
# from langchain.vectorstores.azuresearch import AzureSearch

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
