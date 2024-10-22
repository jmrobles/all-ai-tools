from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.core.security import verify_token
from app.schemas.tool import ToolCreate
from app.services.indexing import index_tool

router = APIRouter()

@router.post("/index")
async def index_documents(tools: List[ToolCreate], token: str = Depends(verify_token)):
    try:
        indexed_tools = []
        for tool in tools:
            indexed_tool = await index_tool(tool)
            indexed_tools.append(indexed_tool)
        return {"status": "success", "message": f"{len(indexed_tools)} tools indexed successfully", "tools": indexed_tools}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")