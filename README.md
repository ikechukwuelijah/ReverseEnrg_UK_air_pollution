# 🌫️ UK Air Pollution Pipeline (Reverse Engineered)

This project reverse-engineers air quality data pipelines for the United Kingdom, ingesting pollution metrics from public APIs and storing them in a PostgreSQL database. The goal is to track key pollutants over time for environmental monitoring, analysis, and forecasting.

## 🎯 Core Objectives

- Retrieve real-time and historical air pollution data by location
- Extract and enrich pollutant levels (e.g. NO₂, PM2.5, O₃) by timestamp and area
- Normalize and store records in PostgreSQL for querying and dashboarding
- Offer insights by pollutant type, source, and geographic trend

## 🧰 Tech Stack

- Python for ETL logic
- Requests + Pandas for data wrangling
- PostgreSQL as destination data store
- Airflow for DAG orchestration
- SQLAlchemy for DB integration
- Document nosql

## 🔄 Pipeline Flow
