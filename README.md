# 🌫️ UK Air Pollution Pipeline (Reverse Engineered)

This project reverse-engineers air quality data pipelines for the United Kingdom, ingesting pollution metrics from public APIs and storing them in a PostgreSQL database. The goal is to track key pollutants over time for environmental monitoring, analysis, and forecasting.

## 🎯 Core Objectives

- Retrieve real-time and historical air pollution data by location
- Extract and enrich pollutant levels (e.g. NO₂, PM2.5, O₃) by timestamp and area
- Normalize and store records in PostgreSQL for querying and dashboarding
- Offer insights by pollutant type, source, and geographic trend

## 🧰 Tech Stack

| Component        | Purpose                        |
|------------------|--------------------------------|
| Python           | Core ETL logic and scripting               |
| Requests         | HTTP client for API interaction                |
| Pandas           | Data wrangling, transformation, and cleaning   |
| SQLAlchemy       | Database ORM and connectivity abstraction           |
| PostgreSQL       | Data warehouse / structured data storage               |
| Apache Airflow   |Workflow orchestration and DAG scheduling |
| Metabase       	 | Business Intelligence (BI) & data visualization |
| Linus	Server     | Hosting / runtime environment|
| Github	         |Version control and CI/CD pipelines                              |
