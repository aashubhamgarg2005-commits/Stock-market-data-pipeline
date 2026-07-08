FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /producer

COPY producer/requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY producer/ /producer/

CMD ["python", "/producer/main.py"]