from typing import Dict
from nemoguardrails.actions import action
import logging
from app.core.agent import run_agent


@action(is_system_action=True)
async def get_ai_tool_info(context: Dict) -> str:
    user_message = context.get('user_message')
    
    try:
        result = await run_agent(user_message)
        return result
    except Exception as e:
        logging.error(f"Error in get_ai_tool_info: {e}")
        return "I'm sorry, but I encountered an error while searching for AI tools. Please try again later."
