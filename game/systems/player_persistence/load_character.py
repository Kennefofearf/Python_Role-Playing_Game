import json
from pathlib import Path


def load_character(name):
    load_dir = Path(__file__).resolve().parents[3] / "saves"

    load_file = load_dir / f"{name}.json"

    with open(load_file, "r") as f:
        loaded_data = json.load(f)

    return loaded_data
