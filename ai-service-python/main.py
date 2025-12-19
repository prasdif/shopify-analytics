from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from agent import ShopifyAgent

load_dotenv()

app = FastAPI(title="Shopify AI Analytics Service")

class QuestionRequest(BaseModel):
    store_id: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    confidence: str

# Initialize Agent
agent = ShopifyAgent(openai_api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def read_root():
    return {"status": "online", "service": "Shopify AI Analytics"}

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
    Endpoint to receive natural language questions about a Shopify store.
    """
    try:
        print(f"Received question for store {request.store_id}: {request.question}")
        
        # 1. Understand Intent & Plan
        # 2. Generate ShopifyQL
        # 3. Execute Query
        # 4. Explain Results
        result = await agent.process_question(request.store_id, request.question)
        
        return AnswerResponse(
            answer=result["answer"],
            confidence=result.get("confidence", "high")
        )
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
