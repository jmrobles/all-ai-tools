.PHONY: help install run db-up db-down lint format test clean

# Variables
PYTHON := poetry run python
UVICORN := poetry run uvicorn
PYTEST := poetry run pytest
ISORT := poetry run isort
BLACK := poetry run black

# Help
help:
	@echo "Available commands:"
	@echo "  install    - Install project dependencies"
	@echo "  run        - Run the FastAPI app in development mode"
	@echo "  run-bot    - Run the Telegram bot locally"
	@echo "  db-up      - Start the PostgreSQL database"
	@echo "  db-down    - Stop the PostgreSQL database"
	@echo "  lint       - Run linters (isort, black)"
	@echo "  format     - Format code using isort and black"
	@echo "  test       - Run tests"
	@echo "  clean      - Remove cached files"
	@echo "  docker-build - Build the Docker image"

# Install dependencies
install:
	@echo "Installing dependencies..."
	poetry install

# Run the FastAPI app
run:
	@echo "Running the FastAPI app..."
	$(UVICORN) app.main:app --reload --host 0.0.0.0 --port 8000

# Database management
db-up:
	@echo "Starting the PostgreSQL database..."
	docker-compose up -d

db-down:
	@echo "Stopping the PostgreSQL database..."
	docker-compose down

# Linting and formatting
lint:
	@echo "Running linters..."
	$(ISORT) --check-only ./app
	$(BLACK) --check ./app

format:
	@echo "Formatting code..."
	$(ISORT) ./app
	$(BLACK) ./app

# Testing
test:
	@echo "Running tests..."
	$(PYTEST)

# Cleaning
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build:
	@echo "Building the Docker image..."
	docker build -t registry.digitalilusion.com/montevive/ai-tool-rag:latest .
push-image:
	@echo "Pushing the Docker image..."
	docker push registry.digitalilusion.com/montevive/ai-tool-rag:latest

rollout:
	kubectl -n montevive rollout restart deployment ai-tool-rag

rollout-bot:
	kubectl -n montevive rollout restart deployment ai-tools-telegram-bot

deploy: docker-build push-image rollout

run-bot:
	@echo "Running the Telegram bot locally..."
	$(PYTHON) -m app.telegram.bot

#
# Default target
.DEFAULT_GOAL := help
