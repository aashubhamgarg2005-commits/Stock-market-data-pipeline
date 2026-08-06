from stockmarketdata-spark-batch:latest

WORKDIR /app
ENV PYTHONPATH=/app
COPY . .

ENV PYTHONUNBUFFERED=1
CMD [ "/opt/spark/bin/spark-submit","/app/spark/loader/loader.py" ]