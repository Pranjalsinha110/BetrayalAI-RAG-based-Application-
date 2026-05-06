from documentLoadAndSplitter import finalChunck
from dotenv import load_dotenv
from langchain_huggingface import   HuggingFaceEndpointEmbeddings,HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
load_dotenv()
import os
os.environ['HF_HOME'] = 'D:/BetrayalAI'
llm = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def embeddingGenerationAndStoring(url:str):
    docs = finalChunck(url)
    if not docs:
        print("none")
        return None
    vectorstore = FAISS.from_documents(
                            documents=docs, 
                            embedding=llm
                                    )
    return vectorstore

