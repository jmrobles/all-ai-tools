# AI Tool RAG System

> This project was created for the [NVIDIA-LlamaIndex Developer Contest](https://developer.nvidia.com/llamaindex-developer-contest).

AI Tool is a Retrieval-Augmented Generation (RAG) system designed to provide information about AI tools based on user queries. It uses LlamaIndex for efficient indexing and retrieval, and pgvector for vector storage. The system offers a FastAPI-based API for document indexing and query processing, as well as a Telegram chatbot interface with Nvidia NeMo Guardrails for enhanced bot behavior. It leverages the OpenAI Agent from LlamaIndex for improved query processing and response generation.

## Demo Video

Want to see the AI Tool RAG System in action? Check out our demonstration video:

[Watch the AI Tool RAG System Demo](https://www.youtube.com/watch?v=SjNkF_0I0V8)

This video showcases the key features and functionality of our system, giving you a firsthand look at how it can help users discover and learn about AI tools.
## Try It Live!

Want to see the AI Tool RAG System in action? You can interact with our live Telegram bot right now!

👉 **[Chat with AllAIToolsBot on Telegram](https://t.me/AllAIToolsBot)**

🚀 **Already Packed with Knowledge:**
- Our bot has information on **over 300 AI tools** in its database!
- We're constantly growing, adding **10 new tools every day**!

Here's what you can do:

1. Click the link above to open the chat with AllAIToolsBot
2. Start a conversation by saying "Hello" or asking about AI tools
3. Try asking questions like:
   - "What are some popular AI tools for content creation?"
   - "Can you recommend an AI tool for image recognition?"
   - "Tell me about the latest AI tools for natural language processing"
   - "What new AI tools were added recently?"

4. Explore the bot's capabilities and see how it leverages our RAG system to provide informative responses about a wide range of AI tools

We'd love to hear your feedback on the bot's performance and any suggestions you might have for improvement. Feel free to open an issue in this repository with your thoughts!

Stay up-to-date with the latest in AI tools - our bot is learning every day! 🧠💡

Happy exploring! 🚀🤖

## Motivation

In today's rapidly evolving AI landscape, there's an abundance of powerful AI tools available, but many of them remain unknown to potential users. While online directories exist, they often lack the ability to provide personalized recommendations based on specific use cases. Our project addresses this gap by offering a simple, quick, and intuitive way to discover AI tools tailored to individual needs.

Key motivations for this project include:

1. **Simplifying AI Tool Discovery**: With the vast number of AI tools available, finding the right one for a specific task can be overwhelming. Our system makes it easy for users to find relevant tools based on their unique requirements.

2. **Personalized Recommendations**: Unlike static directories, our RAG system can understand user queries and provide customized tool suggestions, making it more valuable for users with specific needs.

3. **Accessibility**: By implementing the system as a Telegram bot, we've made it incredibly easy for users to access information about AI tools. There's no need to navigate complex websites or install additional software – users can simply chat with the bot to get the information they need.

4. **Up-to-date Information**: With our system constantly learning and updating its knowledge base, users can stay informed about the latest AI tools and developments in the field.

5. **Bridging the Knowledge Gap**: Many powerful AI tools exist but aren't widely known. Our project helps bridge this gap by making information about these tools more accessible to a broader audience.

By creating this AI Tool RAG System, we aim to empower developers, researchers, and AI enthusiasts to easily discover and leverage the most suitable AI tools for their projects, ultimately accelerating innovation and progress in the field of artificial intelligence.


## Contest Submission

This project is an entry for the NVIDIA-LlamaIndex Developer Contest. It showcases the integration of LlamaIndex, NVIDIA NeMo Guardrails, and other advanced technologies to create a powerful and safe AI tool recommendation system.

## Features

- RAG-based information retrieval for AI tools
- Document indexing using LlamaIndex
- Vector storage with pgvector
- FastAPI-powered API for indexing and querying
- Telegram chatbot interface for user interactions
- Nvidia NeMo Guardrails for enhanced bot behavior and safety
- OpenAI Agent from LlamaIndex for advanced query processing

## Prerequisites

- Python 3.12
- PostgreSQL with pgvector extension
- Poetry
- OpenAI API key
- Telegram Bot API token
- Nvidia NeMo Guardrails library

## Installation


1. Install Poetry if you haven't already:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Clone the repository:

```bash
git clone https://github.com/montevive/ai-tool-rag.git
cd ai-tool-rag
```


3. Install dependencies using Poetry:

```bash
poetry install
```

4. Install the spaCy model for PII data masking:
```bash
poetry run python -m spacy download en_core_web_lg
```

5. Set up your PostgreSQL database with pgvector extension using the provided docker-compose.yml file:

```bash
docker-compose up -d
```

This will start a PostgreSQL database with the pgvector extension installed and ready to use.


6. Configure your environment variables:

```bash
cp .env.example .env
```

Edit the .env file with your database credentials, OpenAI API key, and other necessary configurations:
```bash
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://username:password@localhost/dbname
API_TOKEN=your_api_token_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
NEMO_GUARDRAILS_CONFIG_PATH=nemo_guardrails_config_path
USE_WEBHOOK=false
WEBHOOK_URL=webhook_url
```

## Usage

Activating the Poetry environment
Before running any commands, activate the Poetry environment:

```bash
poetry shell
```

## Starting the Telegram bot service

Run the Telegram bot (if you are running in a local network use the polling mode):

```bash
make run-bot
```
## Staring the API

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000.

## API Endpoints

Before using any endpoint, you need to include a Bearer token in the Authorization header of your requests. The token should be set in your environment variables.


1. Document Indexing:
    - Endpoint: POST /api/index
    - Description: Index a new AI tool document
    - Request Body: JSON object containing tool information
    - Authentication: Bearer token required

2. Query Processing:

    - Endpoint: POST /api/query
    - Description: Process a user query and retrieve relevant AI tools
    - Request Body: JSON object with the user's query
    - Authentication: Bearer token required

For detailed API documentation, visit http://localhost:8000/docs after starting the server.

## Architecture

- FastAPI: Web framework for building the API
- LlamaIndex: Used for document indexing and retrieval
- pgvector: PostgreSQL extension for vector similarity search
- SQLAlchemy: ORM for database interactions
- OpenAI API: Provides the language model backend
- Poetry: Dependency management and packaging
- Telegram Bot API: Interface for the Telegram chatbot
- Nvidia NeMo Guardrails: Enhances bot behavior and safety

## Telegram Bot

The Telegram bot provides a user-friendly interface for interacting with the AI Tool RAG system. Users can send messages to the bot, and it will respond with relevant information about AI tools based on their queries.

## Nvidia NeMo Guardrails

Nvidia NeMo Guardrails is integrated into the system to enhance the bot's behavior and ensure safe interactions. It provides:

- Input validation and sanitization
- Output filtering and safety checks
- Customizable flows for handling user interactions
- Predefined actions for common tasks

The guardrails configuration is located in the `app/guardrails` directory and includes:

- `bot_flows.co`: Defines the conversation flows and checks
- `actions.py`: Custom actions for the guardrails system
- `prompts.yml`: Prompt templates for various tasks
- `config.yml`: Main configuration file for NeMo Guardrails

## OpenAI Agent

The system utilizes the OpenAI Agent from LlamaIndex to process user queries and generate responses. This agent provides:

- Advanced natural language understanding
- Improved context awareness
- More coherent and relevant responses
- Ability to handle complex queries and follow-up questions

The OpenAI Agent is integrated into the core functionality of the RAG system, enhancing its ability to provide accurate and helpful information about AI tools.

## Development

To add new dependencies:

```bash
poetry add package_name
```
To update dependencies:

```bash
poetry update
```
## Development Environment

This project was developed using the following tools and technologies:

- **IDE**: Visual Studio Code
- **AI-assisted Development**: [Continue.dev](https://continue.dev/) extension for VS Code
- **Primary Language Model**: Claude 3.5 Sonnet

We leveraged the power of AI-assisted development to enhance our coding process and improve productivity. The Continue.dev extension in VS Code, coupled with the Claude 3.5 Sonnet model, provided intelligent code suggestions, completions, and generation throughout the development of this project.

## Roadmap

Our project is continuously evolving to improve its capabilities and efficiency. Here's an overview of our current state and future plans:

### Current State

- We have implemented an endpoint to ingest new AI tools into our system.
- Data collection is currently done through web scraping of sources like Reddit and Hacker News.
- A custom data quality pipeline is in place to ensure the integrity and relevance of the ingested data.

### Future Plans

1. **NeMo Curator Integration**: Our next major step is to integrate NVIDIA's NeMo Curator for enhanced data ingestion and quality control. This will allow us to:
   - Automate and improve the data collection process
   - Implement more sophisticated data cleaning and validation techniques
   - Ensure higher quality and more consistent data for our AI tool database

2. **Expanded Data Sources**: We plan to broaden our range of data sources to include more specialized AI and technology forums, blogs, and news sites.

3. **Advanced Analytics**: Implement analytics features to track trending AI tools and provide insights on tool usage and popularity.

4. **User Feedback Loop**: Develop a system to incorporate user feedback and ratings to continually improve our tool recommendations.

5. **Multi-language Support**: Extend the Telegram bot interface to support multiple languages, making the service accessible to a global audience.

6. **API Enhancements**: Expand our API capabilities to allow third-party integrations and more advanced querying options.

We're committed to continually improving the AI Tool RAG System to provide the most up-to-date and relevant information on AI tools to our users. Stay tuned for these exciting updates!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NVIDIA and LlamaIndex for organizing the developer contest and providing the opportunity to showcase this project
- LlamaIndex for the powerful indexing and retrieval library, including the OpenAI Agent
- pgvector for efficient vector storage in PostgreSQL
- FastAPI for the web framework
- OpenAI for the language model API
- Poetry for dependency management
- Telegram Bot API for the chatbot interface
- Nvidia NeMo Guardrails for enhanced bot behavior and safety

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.
