from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class EstimateRequest(BaseModel):
    image_url: str
    description: Optional[str] = None

class EstimateResponse(BaseModel):
    low_estimate: float
    average_estimate: float
    high_estimate: float
    confidence: str
    examples: List[str]

@app.post("/estimate", response_model=EstimateResponse)
async def estimate_value(request: EstimateRequest):
    return EstimateResponse(
        low_estimate=50.0,
        average_estimate=75.0,
        high_estimate=100.0,
        confidence="medium",
        examples=["Similar item sold for $80 last week"]
    )