from pathlib import Path

import yaml
from pyspark.sql import SparkSession


def load_config() -> dict:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main() -> None:
    config = load_config()

    project_root = Path(__file__).resolve().parents[1]
    raw_path = project_root / config["paths"]["raw_input"]
    bronze_path = project_root / config["paths"]["bronze_output"]
    file_format = config["dataset"]["file_format"]
    write_mode = config["pipeline"]["write_mode"]

    raw_files = list(raw_path.glob(f"*.{file_format}"))

    print("Starting bronze ingestion...")
    print(f"Raw input path: {raw_path}")
    print(f"Bronze output path: {bronze_path}")

    if not raw_files:
        print(f"No .{file_format} files found in {raw_path}")
        print("Bronze ingestion stopped.")
        return

    spark = (
        SparkSession.builder
        .appName("bronze-ingestion")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    df = spark.read.format(file_format).load(str(raw_path))
    df.write.mode(write_mode).format("parquet").save(str(bronze_path))

    print("Bronze ingestion completed successfully.")
    spark.stop()


if __name__ == "__main__":
    main()
