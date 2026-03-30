from pathlib import Path

import yaml


def test_config_file_exists() -> None:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "config.yaml"

    assert config_path.exists(), "config.yaml file was not found"


def test_config_has_required_sections() -> None:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    required_sections = ["project_name", "dataset", "paths", "layers", "pipeline"]

    for section in required_sections:
        assert section in config, f"Missing required section: {section}"


def test_config_has_required_paths() -> None:
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "configs" / "config.yaml"

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    required_paths = ["raw_input", "bronze_output", "silver_output", "gold_output"]

    for path_key in required_paths:
        assert path_key in config["paths"], f"Missing required path: {path_key}"
