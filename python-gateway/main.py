from fastapi import FastAPI, HTTPException, Request
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Shopify AI Gateway (Python Fallback)")

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:8000")

@app.post("/api/v1/questions")
async def ask_question(request: Request):
    """
    Acts as a gateway, forwarding the request to the AI Service.
    mimics the Rails backend: POST /api/v1/questions
    """
    try:
        body = await request.json()
        print(f"Gateway received: {body}")
        
        async with httpx.AsyncClient() as client:
            # Forward to AI Service
            response = await client.post(f"{AI_SERVICE_URL}/ask", json=body)
            
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Error from AI Service")
            
            data = response.json()
            return data

    except Exception as e:
        print(f"Gateway Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run on port 3000 to match Rails default
    uvicorn.run(app, host="0.0.0.0", port=3000)
