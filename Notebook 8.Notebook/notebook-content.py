# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "8e5fc2ba-1ca8-43c7-8ed8-ea6ac7ea4ee1",
# META       "default_lakehouse_name": "Central1_LH",
# META       "default_lakehouse_workspace_id": "a0923a92-f29f-42fe-8cb8-9a0acd1a040a",
# META       "known_lakehouses": [
# META         {
# META           "id": "8e5fc2ba-1ca8-43c7-8ed8-ea6ac7ea4ee1"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

#from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
import os

#load_dotenv(override=True) # take environment variables from .env.
key_vault_url = 'https://kv-fabric-usage.vault.azure.net/'
# Variables not used here do not need to be updated in your .env file
endpoint = "https://cpz-ai-search-service.search.windows.net" #os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
AZURE_SEARCH_ADMIN_KEY = mssparkutils.credentials.getSecret(key_vault_url, "cpz-ai-search-service-api-keys")
credential = AzureKeyCredential(AZURE_SEARCH_ADMIN_KEY) #if os.getenv("AZURE_SEARCH_ADMIN_KEY") else DefaultAzureCredential()
index_name = "rag-ai-polygon-index" # os.getenv("AZURE_SEARCH_INDEX", "int-vec")

# endpoint = "https://cel-azure-ai-multi-services-westus.cognitiveservices.azure.com/" #os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
# index_name = "rag-ai-index" # os.getenv("AZURE_SEARCH_INDEX", "int-vec")


account_key = mssparkutils.credentials.getSecret(key_vault_url,"central1fabricpoc-blob-account-key")
blob_connection_string = f"DefaultEndpointsProtocol=https;AccountName=central1fabricpoc;AccountKey=={account_key};EndpointSuffix=core.windows.net" #os.environ["BLOB_CONNECTION_STRING"]
# search blob datasource connection string is optional - defaults to blob connection string
# This field is only necessary if you are using MI to connect to the data source
# https://learn.microsoft.com/azure/search/search-howto-indexing-azure-blob-storage#supported-credentials-and-connection-strings
search_blob_connection_string = "DefaultEndpointsProtocol=https;AccountName=central1fabricpoc;AccountKey={account_key};EndpointSuffix=core.windows.net" #os.getenv("SEARCH_BLOB_DATASOURCE_CONNECTION_STRING", blob_connection_string)
blob_container_name = "central1-input-documents" #os.getenv("BLOB_CONTAINER_NAME", "int-vec")


#azure_openai_endpoint = "https://cpz-open-ai.openai.azure.com/openai/deployments/text-embedding-ada-002/embeddings?api-version=2023-05-15" # os.environ["AZURE_OPENAI_ENDPOINT"]
azure_openai_endpoint = "https://cpz-ai-search-service.search.windows.net/" # os.environ["AZURE_OPENAI_ENDPOINT"]
azure_openai_key = mssparkutils.credentials.getSecret(key_vault_url,"AZURE-OPENAI-KEY")
azure_openai_embedding_deployment = "text-embedding-ada-002" #os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")
azure_openai_model_name = "text-embedding-ada-002" # os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_NAME", "text-embedding-3-large")
azure_openai_model_dimensions = "1536" #int(os.getenv("AZURE_OPENAI_EMBEDDING_DIMENSIONS", 1024))
# This field is only necessary if you want to use OCR to scan PDFs in the data source
azure_ai_services_key = mssparkutils.credentials.getSecret(key_vault_url,"AZURE-AI-SERVICES-KEY")



use_ocr = len(azure_ai_services_key) > 0
#use_ocr = True
# OCR (Optical character recognition) must be used to add page numbers
add_page_numbers = use_ocr

print("use_ocr:",use_ocr)
print("add_page_numbers:",add_page_numbers)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential
import glob
import os

def upload_sample_documents(blob_connection_string, blob_container_name, documents_directory, use_user_identity=False):
    try:
        # Connect to Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=blob_connection_string,
            credential=DefaultAzureCredential() if use_user_identity else None
        )
        container_client = blob_service_client.get_container_client(blob_container_name)

        # Create container if it doesn't exist
        if not container_client.exists():
            container_client.create_container()
            print(f"Container '{blob_container_name}' created.")

        # Get PDF files from directory
        documents_directory = os.path.abspath(documents_directory)
        pdf_files = glob.glob(os.path.join(documents_directory, '*.pdf'))
        print(f"Found {len(pdf_files)} PDF files in {documents_directory}.")

        for file in pdf_files:
            name = os.path.basename(file)
            blob_client = container_client.get_blob_client(name)

            # Check if the blob exists before uploading
            if not blob_client.exists():
                with open(file, "rb") as data:
                    blob_client.upload_blob(data)
                    print(f"Uploaded {name}.")
            else:
                print(f"Blob {name} already exists. Skipping.")

    except Exception as e:
        print(f"Error: {e}")

def upload_documents_without_ocr():
    upload_sample_documents(
        blob_connection_string=blob_connection_string,
        blob_container_name=blob_container_name,
        documents_directory=os.path.join("..", "..", "Microsoft_Fabric_AI/Lamaindex_rag/Dataset", "WellsFargo")
    )

def upload_documents_with_ocr():
    upload_sample_documents(
        blob_connection_string=blob_connection_string,
        blob_container_name=blob_container_name,
        documents_directory=os.path.join("..", "..", "Microsoft_Fabric_AI/Lamaindex_rag/Dataset", "WellsFargo")
    )

# Example Usage
#use_ocr = True  # Set to True if OCR-specific handling is needed

if use_ocr:
    upload_documents_with_ocr()
else:
    upload_documents_without_ocr()

print("use_ocr: ",use_ocr)
print(f"Setup sample data in {'your_container_name'}")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
