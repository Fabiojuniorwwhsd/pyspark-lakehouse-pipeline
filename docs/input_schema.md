# Expected Input Schema

This document describes the minimum expected schema for the raw dataset used in the pipeline.

## Required columns
- `pickup_date` -> date or timestamp used for partitioning and time reference
- `passenger_count` -> number of passengers in the trip
- `trip_distance` -> distance traveled during the trip

## Optional columns
- `fare_amount`
- `payment_type`
- `pickup_location_id`
- `dropoff_location_id`

## Notes
- The pipeline expects the dataset to be stored in `data/raw/`
- Preferred file format: Parquet
- Column names should be standardized before advanced transformations if needed

## Current usage in the project
- `pickup_date` is defined as the partition column in `configs/config.yaml`
- `passenger_count` and `trip_distance` are used in the Gold aggregation step
