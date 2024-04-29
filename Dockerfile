FROM python:latest

USER root

WORKDIR /app

COPY . /app

RUN --mount=type=cache,target=/root/.cache pip install --upgrade --src /usr/src -r requirements.txt


CMD ["python3", "app/index.py" ]