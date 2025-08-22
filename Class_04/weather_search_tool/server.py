import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from main import run_agent


app = FastAPI(title="Tavily Agent Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    prompt: str


class QueryResponse(BaseModel):
    output: str


@app.post("/api/query", response_model=QueryResponse)
async def api_query(req: QueryRequest):
    if not req.prompt or not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")
    try:
        output = await run_agent(req.prompt.strip())
        return QueryResponse(output=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Serve static frontend from ./static
app.mount("/", StaticFiles(directory="static", html=True), name="static")


