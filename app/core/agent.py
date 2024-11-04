from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from app.services.querying import process_query_json
from app.core.config import settings


SYSTEM_PROMPT = """
You are a helpful AI assistant specialized in recommending utilities, products and services that use artificial intelligence. The user provides the use cases that need to be optimized and/or automated and you must respond with the best tools you know to solve them. You must follow these indications: 
- Answer always in English. 
- Try to include the tool's URL always.
- You can't answer anything but the topic: AI tools. 
- Give at last 3 tools.
- If you found similar tools ask to the user for more details for give him a better recommendation
- The "ai_tools_rag" tool expect use cases. Ensure you specify an use case.
"""

def create_openai_agent():
    llm = OpenAI(model="gpt-4o-mini", api_key=settings.OPENAI_API_KEY, temperature=0)

    tools = [
        FunctionTool.from_defaults(
            async_fn=process_query_json,
            name="process_query",
            description="Call this tool to get a ranked JSON array of AI Tools. The tools are ordered by relevance. The query must be in English"
        )
    ]

    agent = OpenAIAgent.from_tools(
        tools,
        system_prompt=SYSTEM_PROMPT,
        llm=llm,
        verbose=True
    )

    return agent

async def run_agent(query: str) -> str:
    agent = create_openai_agent()
    response = await agent.aquery(query)
    return response.response
