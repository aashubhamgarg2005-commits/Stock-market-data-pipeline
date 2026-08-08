from stockmarketdata-spark-batch:latest

WORKDIR /app
ENV PYTHONPATH=/app
COPY . .
RUN pip install --no-cache-dir python-dotenv
RUN wget -O /opt/spark/jars/postgresql-42.7.7.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.7.jar

ENV PYTHONUNBUFFERED=1
CMD [ "/opt/spark/bin/spark-submit","/app/spark/loader/loader.py" ]