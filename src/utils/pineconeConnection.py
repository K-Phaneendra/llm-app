import os
from pinecone import Pinecone
from dotenv import load_dotenv, dotenv_values
from langchain_pinecone import PineconeVectorStore

from src.utils.loadDocuments import (docs, embeddings)

load_dotenv()

pc = Pinecone(api_key=dotenv_values(".env")["PINECONE_API_KEY"])
pcIndex = pc.Index(dotenv_values(".env")['PINECONE_INDEX_NAME'])
index_name = dotenv_values(".env")['PINECONE_INDEX_NAME']

# print('==env==', dotenv_values(".env"))
# delete all records from index
# pcIndex.delete(delete_all=True, namespace="ns")

# storing data in pinecone db
docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name, namespace='ns')

# connect to existing index
# docsearch = PineconeVectorStore.from_existing_index(embeddings=embeddings, index_name=index_name, namespace='ns')
