from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import get_db  
from app.db.tool import DataAITools

router = APIRouter()

@router.get("/stats")
async def get_data_ai_tools_count(db: Session = Depends(get_db)):
    try:
        count = db.query(DataAITools).count()
        return {"status": "success", "count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve stats: {str(e)}")
