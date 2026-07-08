FROM apache/airflow:3.0.2

ENV PYTHONUNBUFFERED=1
WORKDIR /opt/airflow

COPY airflow/requirement.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /tmp/requirements.txt

COPY airflow/ /opt/airflow/

