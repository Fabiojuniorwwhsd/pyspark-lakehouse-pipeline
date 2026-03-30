# Raw Data Folder

This folder is intended to store the raw input dataset used by the pipeline.

## Expected dataset
- NYC Taxi Trips public dataset
- Preferred format: Parquet

## Purpose
Files placed in this folder will be used as the input source for the Bronze ingestion layer.

## Notes
- Keep the raw files unchanged
- Do not manually transform the dataset in this folder
- Bronze ingestion should be the first transformation step
