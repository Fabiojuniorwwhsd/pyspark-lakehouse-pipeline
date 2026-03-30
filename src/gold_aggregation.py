from pathlib import Path

import yaml
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg


def load_config() -> dict:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main() -> None:
    config = load_config()

    project_root = Path(__file__).resolve().parents[1]
    silver_path = project_root / config["paths"]["silver_output"]
    gold_path = project_root / config["paths"]["gold_output"]
    write_mode = config["pipeline"]["write_mode"]

    print("Starting gold aggregation...")
    print(f"Reading silver data from: {silver_path}")
    print(f"Writing gold data to: {gold_path}")

    spark = (
        SparkSession.builder
        .appName("gold-aggregation")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    df = spark.read.format("parquet").load(str(silver_path))

    if "passenger_count" in df.columns and "trip_distance" in df.columns:
        gold_df = (
            df.groupBy("passenger_count")
              .agg(
                  count("*").alias("total_trips"),
                  avg("trip_distance").alias("avg_trip_distance")
              )
        )
    else:
        gold_df = df.limit(100)

    gold_df.write.mode(write_mode).format("parquet").save(str(gold_path))

    print("Gold aggregation completed successfully.")
    spark.stop()


if __name__ == "__main__":
    main()
