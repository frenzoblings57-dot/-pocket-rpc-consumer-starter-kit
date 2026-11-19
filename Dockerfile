FROM python:3.12-slim

WORKDIR /app
COPY pocket_consumer ./pocket_consumer
COPY examples ./examples
ENV PYTHONPATH=/app
ENTRYPOINT ["python", "-m", "examples.query_latest_block"]
