FROM python:3.8.3
ARG RUN_DB_MIGRATIONS_ARG=value
ENV RUN_DB_MIGRATIONS=$RUN_DB_MIGRATIONS_ARG
ENV PYTHONUNBUFFERED 1
RUN ls
COPY requirements.txt /code/
RUN mkdir /code
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code/
