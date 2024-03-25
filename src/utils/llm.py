from src.utils.loadDocuments import (chain, embeddings)
from src.utils.pineconeConnection import (
    docsearch,
    pcIndex)
import openai
import langchain

from dotenv import load_dotenv, dotenv_values

load_dotenv()
# import pinecone


# from langchain.vectorstores import Pinecone
# from langchain_community.vectorstores import Pinecone

openai.api_key = dotenv_values(".env")['OPENAI_API_KEY']


def vector_to_text(vectors):
    texts = []
    for vector in enumerate(vectors):
        response = langchain.query(
            vector, model="text-davinci-003", method='vector-to-text')
        print(response['output'])
        texts.push(response['output'])
    return texts

# def retreive_text_from_database(vector_id):
    # check answer of chatgpt and implement here


def text_to_vector(text):
    vector = embeddings.embed_query(text)
    return vector

# retreive from pinecone index - retreive from pinecone database
# k = top 2


def similaritySearch(query, k=2):
    matching_results = docsearch.similarity_search(query, k=k)
    return matching_results

    # vector = text_to_vector(query)
    # print(vector)
    # matching_results = pcIndex.query(
    #     vector=vector,
    #     top_k=k,
    #     namespace="ns",
    #     include_values=True
    # )

    # matching_results = pcIndex.query(queries=vector, top_k=k)
    # print('in matching==', len(matching_results['matches']))
    # text_results = []
    # for result in matching_results[0].ids:
    #     text = retreive_text_from_database(result)
    #     text_results.append(text)
    # texts = vector_to_text(matching_results['matches'])
    # print('texts===', texts)
    # return matching_results['matches']


# search answers from vector db


def retreive_answers(query):
    # doc_search = retreive_query(query)
    doc_search = similaritySearch(query)
    responseFromVectorDB = chain.run(
        input_documents=doc_search, question=query)

    # responseFromVectorDB = chain.invoke({
    #     "input_documents": doc_search,
    #     "question": query
    # }, return_only_outputs=True)
    return responseFromVectorDB
