FROM apache/spark:python3

USER root

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/spark

# Download required jars in a single layer
RUN set -eux && \
    curl -fsSL https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.5.0/hadoop-aws-3.5.0.jar \
        -o /opt/spark/jars/hadoop-aws-3.5.0.jar && \
    curl -fsSL https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.35.4/bundle-2.35.4.jar \
        -o /opt/spark/jars/bundle-2.35.4.jar && \
    curl -fsSL https://repo1.maven.org/maven2/software/amazon/s3/analyticsaccelerator/analyticsaccelerator-s3/1.3.1/analyticsaccelerator-s3-1.3.1.jar \
        -o /opt/spark/jars/analyticsaccelerator-s3-1.3.1.jar

COPY spark/requirement.txt /tmp/requirements.txt

RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

COPY spark/ /app/