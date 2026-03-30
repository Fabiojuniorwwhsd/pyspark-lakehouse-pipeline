# Architecture Overview

This project follows a lakehouse-style layered architecture using PySpark.

## Layers

### Bronze
Raw data ingestion layer.
- Stores the original dataset with minimal or no transformation
- Preserves the source structure for traceability

### Silver
Cleaned and standardized layer.
- Handles data cleaning
- Standardizes column names and formats
- Applies data quality improvements

### Gold
Business-ready layer.
- Aggregated and curated outputs
- Designed for analytical consumption
- Supports reporting and insights

## Project flow
1. Raw dataset is ingested into the Bronze layer
2. Bronze data is transformed into Silver data
3. Silver data is aggregated into Gold outputs

## Current structure
- `src/bronze_ingestion.py`
- `src/silver_transformation.py`
- `src/gold_aggregation.py`
- `data/`
- `docs/`
- `configs/`
- `tests/`

## Status
Architecture drafted and project structure initialized.
