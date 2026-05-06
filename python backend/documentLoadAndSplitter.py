from youtube import final_text
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def loadDocs(url:str):
    text = final_text(url)
    if not text :
        return None
    doc = Document(
        page_content=text,
        metadata={"source": url,"type": "youtube"}
    )
    return [doc]

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
def splitDocs(docs:list[Document]):
    return splitter.split_documents(docs)

def finalChunck(url:str):
    doc = loadDocs(url)
    if not doc :
        return None
    chunck  = splitDocs(doc)
    return chunck


