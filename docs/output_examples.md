# Expected Output Examples

This document describes the expected type of output for each layer of the pipeline.

## Bronze layer
The Bronze layer stores raw ingested data with minimal transformation.

### Example characteristics
- original columns preserved
- raw records loaded from the input dataset
- stored in Parquet format

## Silver layer
The Silver layer stores cleaned and standardized data.

### Example characteristics
- duplicate rows removed
- null values handled
- fields standardized for downstream processing

## Gold layer
The Gold layer stores aggregated analytical outputs.

### Example example
Grouped by `passenger_count`:
- `passenger_count`
- `total_trips`
- `avg_trip_distance`

## Purpose
These outputs help demonstrate how raw data evolves into business-ready analytical data through the pipeline.
