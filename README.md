# Real-time Crypto Transactions Streaming Data Engineer Project
## Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)

## Introduction
This project demonstrates a real-time streaming data pipeline designed to capture cryptocurrency transactions from major exchange platforms. Leveraging cutting-edge technologies such as Apache Kafka, Apache Spark, AWS, and Airflow, the system is capable of processing over 200 transactions per second, offering scalable, fault-tolerant solutions for handling cryptocurrency data in near real-time.

## Architecture
![Project Architecture](architecture.png)

This project consists of several critical components that work together to ensure real-time streaming and processing of crypto transactions:

- **Data Source**: Using the Tiingo API to generate cryptocurrency data streams.
- **Apache Airflow**: Orchestrates and schedules the entire pipeline, ensuring seamless data ingestion and storage in PostgreSQL.
- **Apache Kafka**: Streams data between various services in a distributed and fault-tolerant manner.
- **ZooKeeper**: keeps track of status of the Kafka cluster nodes and it also keeps track of Kafka topics, and partitions.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: Processes large volumes of data across its distributed nodes.
- **AWS S3**: Final storage for processed data, providing scalability and accessibility.

## Technologies Used
The project leverages a variety of industry-standard tools and platforms, including:

**Python**: Core language for scripting and data manipulation.
**Apache Airflow**: Task orchestration and scheduling.
**Apache Kafka**: Distributed event streaming platform.
**Apache Zookeeper**: Coordination service for managing Kafka nodes.
**Schema Registry**: Ensures schema consistency in Kafka.
**Apache Spark**: Distributed data processing.
**Docker**: Containerization for seamless deployment.
**AWS S3**: Cloud storage for processed data.
  
## Data Source
- Tiingo API: Provides real-time cryptocurrency transaction data, covering over 8,000 tickers from major exchange platforms. [Learn more](https://www.tiingo.com/).

## Highlighted Outcome
- **Real-Time ELT (Extract, Load, Transform)**: Achieved near real-time data ingestion, processing, and storage into AWS S3.
- **Scalability**: Handles over 200 transactions per second, with the ability to scale dynamically based on transaction load.
- **Distributed Synchronization**: Implemented a multi-broker Kafka cluster with data replication to ensure durability and prevent data loss.
- **Pipeline Orchestration**: Apache Airflow orchestrates the pipeline, scheduling tasks for continuous data flow and processing.
- **Schema Management**: Employed schema registry for managing Kafka stream schemas, ensuring data consistency and compatibility across different services.
