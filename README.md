# AI Tool RAG System

AI Tool is a Retrieval-Augmented Generation (RAG) system designed to provide information about AI tools based on user queries. It uses LlamaIndex for efficient indexing and retrieval, and pgvector for vector storage. The system offers a FastAPI-based API for document indexing and query processing.

## Features

- RAG-based information retrieval for AI tools
- Document indexing using LlamaIndex
- Vector storage with pgvector
- FastAPI-powered API for indexing and querying

## Prerequisites

- Python 3.12
- PostgreSQL with pgvector extension
- Poetry
- OpenAI API key


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
5. Set up your PostgreSQL database with pgvector extension.

6. Configure your environment variables:

```bash
cp .env.example .env
```

Edit the .env file with your database credentials, OpenAI API key, and other necessary configurations:
```bash
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://username:password@localhost/dbname
API_TOKEN=your_api_token_here
```

## Usage

Activating the Poetry environment
Before running any commands, activate the Poetry environment:

```bash
poetry shell
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

## Development

To add new dependencies:

```bash
poetry add package_name
```
To update dependencies:

```bash
poetry update
```

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

- LlamaIndex for the powerful indexing and retrieval library
- pgvector for efficient vector storage in PostgreSQL
- FastAPI
- OpenAI
- Poetry
## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.
