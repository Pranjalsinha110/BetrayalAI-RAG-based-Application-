from embeddingGenerationAndStoring import embeddingGenerationAndStoring

def searchAndRetrival(url:str):
    vectorestore = embeddingGenerationAndStoring(url)
    if not vectorestore:
        return None
    return vectorestore.as_retriever(search_kwargs={"k": 2})
    












