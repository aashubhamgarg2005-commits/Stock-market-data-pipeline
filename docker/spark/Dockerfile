FROM apache/spark:4.0.0

USER root

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/spark

COPY spark/requirement.txt /tmp/requirements.txt

RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY spark/ /opt/spark/