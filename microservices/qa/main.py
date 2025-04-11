from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import qa


app = FastAPI(title="Question Answering API")
class QARequest(BaseModel):
    question: str

class QAResponse(BaseModel):
    answer: str
    score: float

@app.post("/qa", response_model=QAResponse)
async def question_answer(request: QARequest):
    """
    Answer a question
    
    Args:
        request: QARequest containing question 
        
    Returns:
        QAResponse containing the answer and additional information
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    result = qa(request.question)
    
    return QAResponse(
        answer=result['answer'],
        score=result['score'],
    )

@app.get("/health")
async def health():
    return {"status": "ok"}
