from typing import List
from sqlalchemy.exc import OperationalError
from app.schemas.tool import ToolCreate, Tool
from llama_index.core import Document, VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore

from sqlalchemy import create_engine, make_url, text
from app.core.config import settings
import asyncio

async def index_tool(tool: ToolCreate) -> Tool:
    
    url = make_url(settings.DATABASE_URL)
    engine = create_engine(url)

    # Check if the tool was previously indexed
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM data_ai_tools WHERE metadata_->>'hash' = :hash"), {"hash": tool.hash})
            
            if result.scalar() > 0:
                print(f"Tool with hash {tool.hash} already indexed. Skipping.")
                return Tool(id=tool.hash, **tool.model_dump())
    except OperationalError as e:
        # Check if the error is due to the missing table.
        if 'relation "data_ai_tools" does not exist' in str(e):
            print(f"Table 'data_ai_tools' does not exist. Skipping indexing for tool with hash {tool.hash}.")
            # Handle the situation when the table does not exist, e.g., returning None or another logic.
            return None
        else:
            # Raise the exception if it is due to other reasons.
            print('damn it')
            return None
    except Exception as e:
        print(f"An error occurred: {e}")


    vector_store = PGVectorStore.from_params(
        database=url.database,
        host=url.host,
        password=url.password,
        port=url.port,
        user=url.username,
        table_name="ai_tools",
        embed_dim=1536,
        hnsw_kwargs={
            "hnsw_m": 16,
            "hnsw_ef_construction": 64,
            "hnsw_ef_search": 40,
            "hnsw_dist_method": "vector_cosine_ops",
        },
    )
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    documents: List[Document] = []
    for idx, use_case in enumerate(tool.use_cases):
        metadata = {
            "name": tool.name,
            "description": tool.description,
            "url": tool.url,
            "categories": ", ".join(tool.categories),
            "dt": str(tool.dt),
            "hash": tool.hash,
            "scrapped": tool.scrapped,
            "latest_scrap": str(tool.latest_scrap),
            "validated": str(tool.validated),
            "use_case_index": str(idx)
        }
        doc = Document(text=use_case, metadata=metadata)
        documents.append(doc)
    
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )
    index.storage_context.persist()
    return Tool(id=tool.hash, **tool.model_dump())

# Helper function to run async code in a synchronous context
def run_async(coro):
    return asyncio.get_event_loop().run_until_complete(coro)
