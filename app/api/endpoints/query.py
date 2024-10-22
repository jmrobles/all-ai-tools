from fastapi import APIRouter, Depends, HTTPException
from app.core.security import verify_token
from app.schemas.tool import Query, QueryResult
from app.services.querying import process_query

router = APIRouter()

@router.post("/query", response_model=QueryResult)
async def process_user_query(query: Query, token: str = Depends(verify_token)):
    try:
        result = await process_query(query.text)
        return QueryResult(query=query.text, results=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query processing failed: {str(e)}")
