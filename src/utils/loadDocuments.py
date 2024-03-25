
# read pdf
# from langchain.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# used to convert text chunks to vectors
# from langchain.embeddings.openai import OpenAIEmbeddings # depricated
from langchain_openai import OpenAIEmbeddings

# llm modal
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

from dotenv import load_dotenv, dotenv_values

load_dotenv()

# read documents folder


def read_docs(documentsPath):
    file_loader = PyPDFDirectoryLoader(documentsPath)
    documents = file_loader.load()
    return documents


docs = read_docs('../../../documents/')


# divide doc into text chunks


# def chunk_data(docs, chunk_size=800, chunk_overlap=50):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size, chunk_overlap=chunk_overlap)
#     doc = text_splitter.split_documents(docs)
#     return doc


# documents = chunk_data(docs=docs)


# embedding technique of openai
embeddings = OpenAIEmbeddings(api_key=dotenv_values(".env")['OPENAI_API_KEY'])

llm = OpenAI(temperature=0.5)
chain = load_qa_chain(llm, chain_type="stuff")
