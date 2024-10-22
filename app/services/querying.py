from typing import List
from app.schemas.tool import Tool, ToolCreate
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.llms.openai import OpenAI
from sqlalchemy import make_url
from app.core.config import settings



async def process_query(query: str) -> List[Tool]:
    url = make_url(settings.DATABASE_URL)
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
    index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context)
    llm = OpenAI(temperature=0.0, model="gpt-4o-mini")

    query_engine = index.as_query_engine(
        simiilarity_top_k=10,
        verbose=True,
        llm=llm
    )
    response = query_engine.query(query)
    
    tools = []
    for node in response.source_nodes:
        metadata = node.metadata
        tool = Tool(
            id=metadata['hash'],
            name=metadata['name'],
            description=metadata['description'],
            url=metadata['url'],
            categories=metadata['categories'].split(', '),
            dt=int(metadata['dt']),
            hash=metadata['hash'],
            scrapped=metadata.get('scrapped'),
            use_cases=[node.text],
            latest_scrap=int(metadata['latest_scrap']),
            validated=metadata['validated'] == 'True',
            rank_score=node.score 
        )
        tools.append(tool)
    
    return tools
