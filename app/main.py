from fastapi import FastAPI
from app.api.endpoints import index, query
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(index.router, prefix="/api", tags=["index"])
app.include_router(query.router, prefix="/api", tags=["query"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
