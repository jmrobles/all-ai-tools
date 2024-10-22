from pydantic import BaseModel
from typing import List, Optional

class ToolCreate(BaseModel):
    name: str
    description: str
    url: str
    categories: List[str]
    dt: int
    hash: str
    scrapped: Optional[str] = None
    use_cases: List[str]
    latest_scrap: int
    validated: bool

class Tool(ToolCreate):
    id: str
    rank_score: Optional[float] = None

    class Config:
        from_attributes = True

class Query(BaseModel):
    text: str

class QueryResult(BaseModel):
    query: str
    results: List[Tool]
