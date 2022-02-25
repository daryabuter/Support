FROM python:3.9

ENV POETRY_VERSION=1.1.13
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update
RUN apt-get install -y libpq-dev python-dev postgresql postgresql-contrib
RUN pip install "poetry==$POETRY_VERSION" && poetry --version

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
  && poetry install
COPY . /app

CMD ["./entrypoint.sh"]
