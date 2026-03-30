from pathlib import Path


def test_required_directories_exist() -> None:
    project_root = Path(__file__).resolve().parents[1]

    required_directories = [
        "data",
        "data/raw",
        "data/bronze",
        "data/silver",
        "data/gold",
        "src",
        "docs",
        "configs",
        "tests",
    ]

    for directory in required_directories:
        dir_path = project_root / directory
        assert dir_path.exists(), f"Missing required directory: {directory}"


def test_required_files_exist() -> None:
    project_root = Path(__file__).resolve().parents[1]

    required_files = [
        "README.md",
        "requirements.txt",
        "configs/config.yaml",
        "docs/architecture.md",
        "src/bronze_ingestion.py",
        "src/silver_transformation.py",
        "src/gold_aggregation.py",
    ]

    for file_name in required_files:
        file_path = project_root / file_name
        assert file_path.exists(), f"Missing required file: {file_name}"
