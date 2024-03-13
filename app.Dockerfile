FROM python:3.11 as requirements-stage
WORKDIR /tmp
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
FROM python:3.11
WORKDIR /code
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy databases python-dotenv psycopg2 requests
COPY app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
