from pathlib import Path

import yaml
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def load_config() -> dict:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main() -> None:
    config = load_config()

    project_root = Path(__file__).resolve().parents[1]
    bronze_path = project_root / config["paths"]["bronze_output"]
    silver_path = project_root / config["paths"]["silver_output"]
    write_mode = config["pipeline"]["write_mode"]

    print("Starting silver transformation...")
    print(f"Reading bronze data from: {bronze_path}")
    print(f"Writing silver data to: {silver_path}")

    spark = (
        SparkSession.builder
        .appName("silver-transformation")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    df = spark.read.format("parquet").load(str(bronze_path))

    cleaned_df = (
        df.dropDuplicates()
          .dropna()
    )

    cleaned_df.write.mode(write_mode).format("parquet").save(str(silver_path))

    print("Silver transformation completed successfully.")
    spark.stop()


if __name__ == "__main__":
    main()
