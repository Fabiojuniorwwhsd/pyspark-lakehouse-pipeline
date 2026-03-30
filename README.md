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
- `src/bronze_ingestion.py` -> raw data ingestion placeholder
- `src/silver_transformation.py` -> data cleaning and standardization placeholder
- `src/gold_aggregation.py` -> aggregated output generation placeholder
- `configs/config.yaml` -> project configuration
- `docs/architecture.md` -> architecture overview
- `data/` -> storage for raw and processed layers
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

2. Run the pipeline modules individually:
   - `python src/bronze_ingestion.py`
   - `python src/silver_transformation.py`
   - `python src/gold_aggregation.py`

## Current status
Project structure initialized with:
- layered pipeline modules
- configuration file
- architecture documentation
- execution requirements

This project is currently in the setup and development phase.

## Next steps
- connect the real dataset ingestion
- implement PySpark transformations
- create Bronze, Silver and Gold outputs
- add data quality checks
- include tests and execution examples
