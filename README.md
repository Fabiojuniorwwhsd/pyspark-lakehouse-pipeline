# PySpark Lakehouse Pipeline

Lakehouse-style data pipeline using PySpark and layered architecture.

## Project overview
This project simulates a data engineering pipeline using PySpark and a lakehouse-inspired structure with Bronze, Silver and Gold layers.

The goal is to organize a scalable flow that starts with raw data ingestion, moves through cleaning and standardization, and ends with business-ready aggregated outputs.

## Dataset
- **Source:** NYC Taxi Trips public dataset
- **Format:** Parquet
- **Use case:** simulate a batch data pipeline with layered transformations

## Architecture
This project follows a layered architecture:

### Bronze
Raw data ingestion layer.
- Stores the original dataset
- Preserves traceability
- Minimizes early transformation

### Silver
Cleaned and standardized layer.
- Applies data cleaning
- Standardizes structure and fields
- Improves data quality

### Gold
Business-ready layer.
- Produces aggregated outputs
- Organizes analytical data
- Supports reporting and downstream consumption

## Current project structure
- `src/bronze_ingestion.py` -> raw data ingestion with PySpark and config loading
- `src/silver_transformation.py` -> cleaning and standardization logic
- `src/gold_aggregation.py` -> analytical aggregation logic
- `configs/config.yaml` -> project configuration
- `docs/architecture.md` -> architecture overview
- `docs/input_schema.md` -> expected raw dataset schema
- `data/raw/` -> input dataset location
- `data/bronze/` -> raw ingested outputs
- `data/silver/` -> cleaned and standardized outputs
- `data/gold/` -> aggregated analytical outputs
- `notebooks/` -> optional exploration and testing
- `tests/` -> future tests and validations

## Planned pipeline flow
1. Ingest raw trip data into the Bronze layer
2. Transform Bronze data into cleaned Silver data
3. Aggregate Silver data into Gold outputs

## Technologies
- PySpark
- Python
- YAML
- Pandas
- Jupyter

## Configuration
Pipeline settings are centralized in `configs/config.yaml`, including:
- dataset information
- input and output paths
- layer descriptions
- partition column
- write mode

## How to run
1. Install dependencies:
   `pip install -r requirements.txt`

2. Place the input dataset in:
   `data/raw/`

3. Run the pipeline modules in order:
   - `python src/bronze_ingestion.py`
   - `python src/silver_transformation.py`
   - `python src/gold_aggregation.py`

## Current status
Project currently includes:
- layered pipeline structure
- configuration file with paths and settings
- architecture documentation
- Bronze ingestion script with PySpark and YAML config loading
- Silver transformation script with basic cleaning logic
- Gold aggregation script with analytical output generation
- execution requirements and environment ignore rules

This project is currently in active development.

## Next steps
- add a real sample dataset for testing
- improve Silver transformations with stronger validation rules
- refine Gold aggregations with more analytical outputs
- add tests for configuration and pipeline execution
- document expected input schema
