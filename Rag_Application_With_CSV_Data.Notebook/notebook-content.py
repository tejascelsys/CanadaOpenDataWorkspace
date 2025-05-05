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

# CELL ********************

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Load the CSV file
df = spark.read.format("csv").option("header", "true").load("abfss://CanadaOpenDataWorkSpace@onelake.dfs.fabric.microsoft.com/Real_Time_Local_Business_Index_LH.Lakehouse/Files/33100398-eng/33100398.csv")

# Show the data
df.show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%pip install langchain openai sentence-transformers pandas


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd

# Load CSV into a Pandas DataFrame
csv_file_path = "abfss://CanadaOpenDataWorkSpace@onelake.dfs.fabric.microsoft.com/Real_Time_Local_Business_Index_LH.Lakehouse/Files/33100398-eng/33100398.csv"
data = pd.read_csv(csv_file_path)

# Combine relevant columns into a single string for context (e.g., row-wise aggregation)
data['context'] = data.apply(lambda row: " | ".join(map(str, row.values)), axis=1)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install -U langchain-community

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install tiktoken

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from langchain.llms import OpenAI

# Azure OpenAI configuration
openai_api_key = "9e6d4742ab2a4f32bbbb9585291def02"
openai_api_base = "https://cel-azure-ai-services.cognitiveservices.azure.com/"
openai_api_version = "2023-05-15"  # Use the correct API version
openai_deployment_name = "text-embedding-ada-002"  # Your Azure OpenAI deployment name

# Initialize the OpenAI LLM with Azure-specific configurations
llm = OpenAI(
    api_type="azure",
    api_base=openai_api_base,
    api_key=openai_api_key,
    deployment_name=openai_deployment_name,
    api_version=openai_api_version
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    api_type="azure",
    api_base=openai_api_base,
    api_key=openai_api_key,
    deployment="text-embedding-ada-002" ,  # Adjust this if required
    api_version=openai_api_version
)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Initialize LLM
llm = OpenAI(deployment="gpt-35-turbo-16k", azure_openai_key="9e6d4742ab2a4f32bbbb9585291def02")

# Create RAG chain
retriever = vector_store.as_retriever()
rag_chain = RetrievalQA(llm=llm, retriever=retriever)

# Ask a question
query = "What is the summary of the data ?"
response = rag_chain.run(query)
print(response)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%pip install langchain faiss-cpu sentence-transformers openai pandas

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install openai


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install openai==0.28

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install --upgrade openai


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install --upgrade pip

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import openai

# Azure OpenAI Configuration
openai_api_key = "ca587497e01b4f39bc878b48a0682ce9"  # Replace with your Azure OpenAI API key
openai_api_base = "https://cel-azure-ai-services.cognitiveservices.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15"  # Replace with your Azure resource name
openai_api_version = "2023-05-15"  # Use the correct API version
embedding_deployment_name = "text-embedding-ada-002"  # Name of your Azure-deployed embedding model

# Test Embedding
try:
    # Create Embedding
    response = openai.Embedding.create(
        input="This is a test for embedding.",
        engine="text-embedding-ada-002"  # Replace with your deployment name
    )
    print(response)
except Exception as e:
    print(f"Error: {e}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install -U langchain-community

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install tiktoken

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install -U langchain-community

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

pip install tiktoken

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Step 1: Install required libraries
# Uncomment and run this if needed
#%pip install langchain faiss-cpu sentence-transformers openai pandas

# Step 2: Import necessary libraries
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Step 3: Load the CSV data
# Replace with your actual CSV file path
csv_file_path = "abfss://CanadaOpenDataWorkSpace@onelake.dfs.fabric.microsoft.com/Real_Time_Local_Business_Index_LH.Lakehouse/Files/33100398-eng/33100398.csv"
data = pd.read_csv(csv_file_path)

# Step 4: Preprocess the CSV data
# Combine all columns in each row into a single string for vectorization
data['context'] = data.apply(lambda row: " | ".join(row.astype(str)), axis=1)

# Step 5: Configure Azure OpenAI embeddings
openai_api_key = "9e6d4742ab2a4f32bbbb9585291def02"  # Replace with your Azure OpenAI API key
openai_api_base = "https://cel-azure-ai-services.cognitiveservices.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15"  # Replace with your Azure resource name
openai_api_version = "2023-05-15"  # Use the correct API version
embedding_deployment_name = "text-embedding-ada-002"  # Name of your Azure-deployed embedding model
llm_deployment_name = "gpt-35-turbo-16k"  # Your GPT model deployment name

# Step 5: Initialize the Azure OpenAI Embeddings
embeddings = OpenAIEmbeddings(
    deployment=embedding_deployment_name,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    openai_api_version=openai_api_version,
    openai_api_type="azure"
)

# Step 6: Create the FAISS vector store
print("Creating FAISS vector store...")
vector_store = FAISS.from_texts(data['context'].tolist(), embeddings)
print("FAISS vector store created successfully!")

# Step 7: Initialize Azure OpenAI LLM
llm = AzureOpenAI(
    deployment_name=llm_deployment_name,
    openai_api_key=openai_api_key,
    openai_api_base=openai_api_base,
    openai_api_version=openai_api_version,
    openai_api_type="azure"
)

# Step 8: Set up the Retrieval-Augmented Generation (RAG) Chain
retriever = vector_store.as_retriever()
rag_chain = RetrievalQA(llm=llm, retriever=retriever)

# Step 9: Test the RAG system
query = "What insights can you provide about the product data in the CSV?"
response = rag_chain.run(query)

# Step 10: Print the response
print("Response from RAG system:")
print(response)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

VarA="hello"


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Set the mean and standard deviation
mu, sigma = 0, 0.1 

# Generate a normally distributed variable
var = np.random.normal(mu, sigma, 1000)

# Create a histogram of the variable using seaborn's histplot
sns.histplot(var, bins=30, kde=True)

# Add title and labels
plt.title('Histogram of Normally Distributed Variable')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
