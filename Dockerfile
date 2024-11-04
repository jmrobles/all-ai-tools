FROM python:3.12.3-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
RUN python -m spacy download en_core_web_lg
COPY . /app
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
