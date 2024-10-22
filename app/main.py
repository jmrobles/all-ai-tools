from fastapi import FastAPI
from app.api.endpoints import index, query, stats
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(index.router, prefix="/api", tags=["index"])
app.include_router(query.router, prefix="/api", tags=["query"])
app.include_router(stats.router, prefix="/api", tags=["stats"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
