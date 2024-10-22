FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
COPY . /app
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
