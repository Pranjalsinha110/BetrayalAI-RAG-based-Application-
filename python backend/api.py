from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from main import getAnswer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class Query(BaseModel):
    url :str
    query :str
    session_id :str

@app.post("/getAnswer")
def ask_Question_And_Url(data :Query):
    try:
        answer = getAnswer(data.session_id,data.url,data.query)
        print("DEBUG ANSWER:", answer)
        if not answer:
            raise HTTPException(status_code=404, detail="Answer not found.")
        return{
            "url":data.url,
            "query":data.query,
            "answer":answer
        }
    except Exception as e:
         
        raise HTTPException(status_code=500, detail=str(e))
        