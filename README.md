📈 Real-Time Stock Market Data Engineering Pipeline

An end-to-end, production-inspired data engineering pipeline designed to ingest, process, store, orchestrate, and monitor real-time and batch stock market data using modern data engineering technologies.

The project demonstrates a scalable data platform architecture using REST APIs, Kafka, Apache Spark, Apache Airflow, MinIO, Docker, Prometheus, and Grafana.

---

🏗️ Architecture

flowchart LR
    A[📡 Finnhub REST API / WebSocket] --> B[🐍 Python Data Producer]

    B --> C{Processing Mode}

    C -->|Batch| D[⏰ Airflow Scheduler]
    C -->|Streaming| E[📨 Apache Kafka]

    D --> F[🧩 Apache Spark]
    E --> F

    F --> G[🥉 Bronze Layer]
    G --> H[🥈 Silver Layer]
    H --> I[🥇 Gold Layer]

    G --> J[(🪣 MinIO / S3 Data Lake)]

    H --> J
    I --> J

    F --> K[📊 Prometheus]
    K --> L[📈 Grafana]

    D --> M[🔍 Airflow Monitoring]

---

🚀 Key Features

- 📡 Ingests stock market data from external financial APIs
- 🔄 Supports both batch and real-time streaming pipelines
- 📨 Kafka-based event streaming architecture
- ⚡ Distributed processing using Apache Spark
- 🪣 S3-compatible data lake using MinIO
- 🥉 Bronze, Silver, and Gold data layers
- ⏰ Workflow orchestration using Apache Airflow
- 🐳 Fully containerized using Docker
- 📊 Monitoring using Prometheus and Grafana
- 🔁 Incremental data processing using state management
- 📁 Parquet-based optimized data storage
- 🧱 Modular and scalable project architecture
- 📝 Centralized logging and error handling

---

🛠️ Tech Stack

Programming

- Python
- SQL

Data Engineering

- Apache Kafka
- Apache Spark
- Spark Structured Streaming
- Apache Airflow

Storage

- MinIO
- Amazon S3-compatible object storage
- Parquet

DevOps & Infrastructure

- Docker
- Docker Compose
- Linux / WSL

Monitoring

- Prometheus
- Grafana

Data Source

- Finnhub Stock Market API

---

📂 Project Structure

real-time-stock-market-pipeline/
│
├── producer/
│   ├── api/
│   │   ├── base_client.py
│   │   └── finnhub_client.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── constants.py
│   │
│   ├── state/
│   │   └── state.json
│   │
│   ├── writer/
│   │   └── minio_writer.py
│   │
│   └── main.py
│
├── spark/
│   ├── jobs/
│   │   ├── batch_job.py
│   │   └── streaming_job.py
│   │
│   ├── consumer/
│   │   └── spark_consumer.py
│   │
│   └── config/
│       └── spark_config.py
│
├── airflow/
│   └── dags/
│       └── stock_market_pipeline.py
│
├── storage/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── docker/
│   ├── Dockerfile.producer
│   ├── Dockerfile.spark
│   └── Dockerfile.airflow
│
├── docker-compose.yml
├── .env.example
├── Makefile
├── requirements.txt
└── README.md

---

🔄 Data Pipeline Flow

1️⃣ Data Ingestion

The pipeline collects stock market data from the Finnhub API.

The following types of data can be ingested:

- 📊 Real-time stock quotes
- 📈 Historical candles
- 🏢 Company profiles
- 📰 Company news
- 💰 Earnings data
- 📑 Financial statements
- 🌍 Market status

---

2️⃣ Batch Processing

The batch pipeline is designed for periodic data extraction and processing.

Finnhub API
     ↓
Python Producer
     ↓
State Manager
     ↓
MinIO - Raw/Bronze Layer
     ↓
Apache Spark
     ↓
Silver Layer
     ↓
Gold Layer

The pipeline uses state management to track the last successful execution and prevent unnecessary duplicate processing.

---

3️⃣ Streaming Processing

The real-time streaming pipeline follows an event-driven architecture.

Stock Market Data
        ↓
Python Producer
        ↓
Apache Kafka
        ↓
Spark Structured Streaming
        ↓
Bronze Layer
        ↓
Silver Layer
        ↓
Gold Layer
        ↓
MinIO Data Lake

Kafka provides a reliable buffer between data producers and Spark consumers.

---

🗂️ Data Lake Architecture

The project follows a multi-layer data lake architecture.

🥉 Bronze Layer

Stores raw data in its original form.

API / Kafka
    ↓
Raw JSON
    ↓
Bronze Layer

Characteristics:

- Raw data
- Minimal transformation
- Original source structure preserved
- Useful for reprocessing and auditing

---

🥈 Silver Layer

Contains cleaned and standardized data.

Typical transformations:

- Schema enforcement
- Data type conversion
- Null handling
- Deduplication
- Timestamp normalization
- Data validation

---

🥇 Gold Layer

Contains business-ready analytical data.

Examples:

- Daily stock performance
- Price movement analysis
- Trading volume trends
- Company-level metrics
- Market performance indicators

---

📨 Kafka Architecture

Kafka is used for real-time data streaming.

Producer
   ↓
Kafka Topic
   ↓
Spark Structured Streaming

Possible topics:

stock-quotes
stock-candles
company-news
company-earnings
financial-data
market-status

Kafka enables:

- High-throughput ingestion
- Fault tolerance
- Decoupled producers and consumers
- Real-time event processing

---

⚡ Apache Spark Processing

Apache Spark is used for large-scale batch and streaming data processing.

Batch Processing

SparkSession
      ↓
Read Data
      ↓
Transform Data
      ↓
Write Parquet

Streaming Processing

Kafka
  ↓
Spark Structured Streaming
  ↓
Transformations
  ↓
MinIO / S3

Spark is configured with S3A support to communicate with MinIO as an S3-compatible storage system.

---

🪣 MinIO Data Lake

MinIO acts as the local S3-compatible object storage layer.

Example bucket structure:

stock-market-data/
│
├── bronze/
│   ├── quotes/
│   ├── candles/
│   └── news/
│
├── silver/
│   ├── quotes/
│   └── candles/
│
└── gold/
    ├── daily-performance/
    └── market-summary/

The data is stored in Parquet format for efficient analytical processing.

---

⏰ Apache Airflow

Airflow is responsible for workflow orchestration.

Example workflow:

Start
  ↓
Extract Stock Data
  ↓
Validate Data
  ↓
Run Spark Job
  ↓
Write Silver Data
  ↓
Create Gold Data
  ↓
Validate Pipeline
  ↓
End

Airflow provides:

- Scheduling
- Dependency management
- Retry mechanisms
- Task monitoring
- Pipeline failure handling

---

📊 Monitoring & Observability

The pipeline includes monitoring using:

Prometheus

Collects metrics such as:

- Pipeline execution status
- Processing latency
- Record counts
- Kafka metrics
- Spark job metrics
- API request metrics

Grafana

Provides dashboards for:

- Pipeline health
- Processing performance
- API activity
- Kafka throughput
- System resource usage

Example:

Application / Services
        ↓
Metrics
        ↓
Prometheus
        ↓
Grafana Dashboard

---

🐳 Dockerized Architecture

All major services are containerized using Docker.

┌─────────────────────────────┐
│        Docker Compose       │
├─────────────────────────────┤
│                             │
│  Kafka                       │
│  Spark                       │
│  Airflow                     │
│  MinIO                       │
│  Prometheus                  │
│  Grafana                     │
│                             │
└─────────────────────────────┘

Benefits:

- Reproducible environment
- Easy setup
- Service isolation
- Environment consistency
- Portable deployment

---

⚙️ Getting Started

Prerequisites

Make sure you have the following installed:

- Docker Desktop
- Docker Compose
- Git
- Python 3.10+
- WSL2 / Linux environment recommended

---

1️⃣ Clone the Repository

git clone https://github.com/your-username/real-time-stock-market-pipeline.git

cd real-time-stock-market-pipeline

---

2️⃣ Configure Environment Variables

Create a ".env" file:

FINNHUB_API_KEY=your_api_key

MINIO_ROOT_USER=admin
MINIO_ROOT_PASSWORD=your_password

KAFKA_BOOTSTRAP_SERVERS=kafka:9092

«Never commit your actual ".env" file to GitHub.»

---

3️⃣ Start the Services

docker compose up -d

Check running containers:

docker ps

---

4️⃣ Run the Pipeline

Start the batch pipeline:

python producer/main.py

Run Spark processing:

spark-submit spark/jobs/batch_job.py

For streaming:

spark-submit spark/jobs/streaming_job.py

---

📈 Example Data Flow

External Stock API
        ↓
    Data Producer
        ↓
   Data Validation
        ↓
    ┌───────────┐
    │           │
  Batch      Streaming
    │           │
    ↓           ↓
 MinIO       Kafka
    │           │
    └─────┬─────┘
          ↓
        Spark
          ↓
      Bronze
          ↓
       Silver
          ↓
        Gold
          ↓
       MinIO
          ↓
   Analytics Layer

---

🔐 Data Engineering Best Practices Implemented

- Environment variables for secrets
- Modular project structure
- Incremental processing
- State management
- Structured logging
- Data lake layering
- Parquet optimization
- Containerized services
- Fault-tolerant streaming
- Pipeline monitoring
- Separation of ingestion and processing
- Reproducible development environment

---

🎯 Project Objectives

The main objective of this project is to demonstrate the design and implementation of a modern data engineering platform capable of handling both batch and streaming stock market data.

This project focuses on:

- Real-time data ingestion
- Distributed data processing
- Event-driven architecture
- Data lake design
- Workflow orchestration
- Monitoring and observability
- Docker-based infrastructure

---

🚀 Future Enhancements

- [ ] Add Apache Iceberg or Delta Lake
- [ ] Add data quality checks using Great Expectations
- [ ] Add dbt transformation layer
- [ ] Deploy pipeline to cloud infrastructure
- [ ] Add CI/CD using GitHub Actions
- [ ] Add real-time analytics dashboard
- [ ] Add machine learning-based stock prediction
- [ ] Add schema registry for Kafka
- [ ] Add alerting through Grafana
- [ ] Add Kubernetes deployment

---

📊 Project Status

✅ Project Architecture
✅ API Integration
✅ Data Producer
✅ Kafka Integration
✅ MinIO Storage
✅ Bronze Layer
✅ Spark Batch Processing
🔄 Spark Streaming Processing
🔄 Airflow Orchestration
🔄 Prometheus Monitoring
🔄 Grafana Dashboard
🚀 Production Optimization

---

🧠 Key Learning Outcomes

Through this project, I gained practical experience in:

- Designing end-to-end data pipelines
- Building batch and streaming architectures
- Working with Apache Kafka
- Processing data using Apache Spark
- Implementing S3-compatible data lakes
- Orchestrating workflows using Airflow
- Containerizing applications with Docker
- Implementing monitoring using Prometheus and Grafana
- Handling incremental data processing
- Designing scalable data engineering systems

---

👨‍💻 Author

Shubham Garg

B.Tech CSE — Data Science

Aspiring Data Engineer

---

⭐ If You Found This Project Useful

If you find this project interesting, consider giving it a ⭐ on GitHub!

---

«This project is built for educational and portfolio purposes to demonstrate modern data engineering concepts and production-inspired pipeline architecture.»