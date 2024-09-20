# Real-time Crypto Transactions Streaming Data Engineer Project
## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)

## Introduction
This Project aims to build an end-to-end streaming data engineering pipeline to capture transactions among various cryptocurrencies from major cryptocurrency exchange platforms in near real-time. It covers each stage from data ingestion to processing and finally to storing, leveraging Python, airflow, Kafka, Pyspark and Amazon Web services(AWS).
## Architecture
![Project Architecture](architecture.png)

The project is designed with the following components:

**Data Source**: I use Tinngo API to generate random user data for the pipeline.
**Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
**Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
**Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
**Apache Spark**: For data processing with its master and worker nodes.
**AWS S3**: Where the processed data will be stored.

## Technologies Used
- Python
- Apache Airflow
- Apache Kafka
- Apache Zookeeper
- Control Center and Schema Registry
- Apache Spark
- Docker
- AWS S3
  
## Data 
- Crypto transaction Data is generated by Tiingo API (https://www.tiingo.com/) which covers over 8000 tickers for major cryptocurrency exchange platforms.

## Highlighted Outcome
- **Real-Time ELT**: Achieved near real-time data ingestion, processing, and loading into the s3.
- **Scalability:**: Capable of handling over 200 transactions per second in real-time streaming, with the ability to seamlessly scale up or down in response to fluctuations in transaction volume
- **Distributed Synchronization**: Implemented a multi-broker Kafka cluster with replica synchronization to prevent data loss, ensuring durability and scalability.
- **Pipeline Orchestration with Airflow**: Orchestrate the data pipeline, scheduling tasks to ensure continuous data flow and processing using Airflow
Schema Management: Employed glue scheme registry to manage and monitor Kafka stream schemas changes, ensuring data consistency and compatibility.
