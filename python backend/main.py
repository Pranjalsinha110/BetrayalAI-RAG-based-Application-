from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# from searchAndRetrieval import searchAndRetrival
from embeddingGenerationAndStoring import embeddingGenerationAndStoring
from dotenv import load_dotenv
import os
load_dotenv()
os.environ['HF_HOME'] = 'D:/BetrayalAI'
llm = HuggingFacePipeline.from_model_id(model_id="microsoft/Phi-3-mini-4k-instruct",task="text-generation",   
                        pipeline_kwargs=dict(
                            temperature = 0.5,
                            max_new_tokens = 150,
                            return_full_text = False,
                            trust_remote_code=True
                            
                        )
    )



model = llm
parser = StrOutputParser()


session_store = {}

prompt = PromptTemplate(
    input_variables=["context","query"],

   template="""
Answer ONLY using the context.

RULES:
- Give ONLY the final answer
- No explanation
- No "Human:" or prompt repetition
- No extra text

Context:
{context}

Question:
{query}

Answer:
"""
)

def getretriever(session_id:str, url:str):
    if len(session_store) > 100:  
        session_store.clear()

    if session_id in session_store:
        stored = session_store[session_id]

        if stored["url"]==url:
            return stored["retriever"]
    
    vectorestore = embeddingGenerationAndStoring(url)
    if not vectorestore:
        return None
    retriever = vectorestore.as_retriever(search_kwargs={"k": 2})
    session_store[session_id] = {
        "url": url,
        "retriever": retriever
    }
    return retriever

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])





def getAnswer(session_id:str, url:str, query:str):
    retriever = getretriever(session_id, url)

    if not retriever:
        return "I could not retrieve any information from the provided URL."
    docs = retriever.invoke(query)
    context = format_docs(docs)
    
    
    final_chain =  prompt  | model | parser
    result = final_chain.invoke({
        "context":context,
        "query":query
    })

    if "Answer" in result:
        result = result.split("Answer:")[-1]
    clean_answer = result.split("Question:")[0].strip()
    return clean_answer


