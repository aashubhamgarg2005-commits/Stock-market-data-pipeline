FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/:/producer

WORKDIR /producer

COPY producer/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

COPY producer/ /producer/
COPY Minio_client/ /Minio_client/

CMD ["python", "/producer/main.py"]