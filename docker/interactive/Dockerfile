# --- Stage 1: Build ---
FROM python:3.9.15-slim as build

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential \
    gcc

WORKDIR /app
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:${PATH}"

COPY requirements.txt .
RUN pip install -r requirements.txt

# -- Stage 2: Final ---
FROM python:3.9.15-slim

RUN groupadd python && \
    useradd -r -g python python

RUN mkdir /app && \
    chown python:python /app

WORKDIR /app

COPY --chown=python:python --from=build /app/venv ./venv
COPY --chown=python:python . .

USER python

ENV PATH="/app/venv/bin:${PATH}"
CMD ["python", "main.py"]
