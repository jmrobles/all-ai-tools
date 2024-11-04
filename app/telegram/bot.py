import os
import sys
import logging
from urllib.parse import urlparse
from telegram import Update
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from nemoguardrails import LLMRails, RailsConfig
from app.core.config import settings

# Set up logging
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL), format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize NeMo Guardrails
def init_guardrails():
    try:
        config_path = settings.NEMO_GUARDRAILS_CONFIG_PATH
        logger.info(f"Initializing NeMo Guardrails with config path: {config_path}")
        
        if not os.path.isdir(config_path):
            raise FileNotFoundError(f"Config folder not found: {config_path}")
        config = RailsConfig.from_path(str(config_path))
        rails = LLMRails(config=config)
        logger.info("NeMo Guardrails initialized successfully")
        return rails
    except Exception as e:
        logger.error(f"Error initializing NeMo Guardrails: {e}", exc_info=True)
        raise

try:
    guardrails = init_guardrails()
except Exception as e:
    logger.error(f"Failed to initialize guardrails: {e}")
    guardrails = None
    sys.exit(-1)




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hi! I'm an AI Tool Assistant. How can I help you today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Ask me about AI tools and I'll do my best to help!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the user message and respond using the RAG system with guardrails."""
    user_input = update.message.text
    try:
        await update.message.reply_text(
            "_Let me think, please wait..._",
            parse_mode=ParseMode.MARKDOWN
        )
        response = await guardrails.generate_async(user_input)
        if not response:
            response = "I'm sorry, I couldn't generate a proper response. Could you please rephrase your question?"
        
        # Send the response with markdown parsing enabled
        await update.message.reply_text(
            response,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True
        )
    except BadRequest as br:
        # Handle markdown parsing errors
        logging.error(f"Error parsing markdown: {br}")
        await update.message.reply_text(
            "I encountered an error while formatting the response." 
        )
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        await update.message.reply_text("I'm sorry, but I encountered an error while processing your request. Please try again later.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    if settings.USE_WEBHOOK:
        parsed_url = urlparse(settings.WEBHOOK_URL)
        url_path = parsed_url.path.lstrip('/')
        webhook_url = settings.WEBHOOK_URL
        
        logger.info(f"Running webhook with url_path: {url_path}")
        logger.info(f"Webhook URL: {webhook_url}")
        
        application.run_webhook(listen="0.0.0.0", port=8000, webhook_url=webhook_url, url_path=url_path, allowed_updates=Update.ALL_TYPES)
    else:
        application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
