import hashlib
import json
import os
import sys
from pathlib import Path

import toml

from db import add_config


def load_config(filepath: str):
    return toml.load(filepath)


def hash_dict(d):
    """Recursively hashes a dictionary."""
    # Convert the dictionary to a JSON string with sorted keys to ensure consistent ordering
    json_str = json.dumps(d, sort_keys=True)
    # Create a SHA-256 hash object
    hash_obj = hashlib.sha256()
    # Update the hash object with the JSON string encoded as bytes
    hash_obj.update(json_str.encode("utf-8"))
    # Return the hexadecimal representation of the hash
    return hash_obj.hexdigest()


def create_partial_configs(path_to_consolidated_config: str | Path):
    path_to_consolidated_config = Path(path_to_consolidated_config)
    assert (
        path_to_consolidated_config.exists()
    ), f"No consolidated config in {path_to_consolidated_config}!"

    consolidated_config = load_config(path_to_consolidated_config)

    for config, value in consolidated_config.items():
        if config == "wildcards":
            continue

        db_config_id = add_config(value["config"])
        file = "{}/{}.{}".format(value["final_folder"], db_config_id, value["format"])

        # create file if it does not exist
        if not os.path.exists(file):
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, "w") as f:
                toml.dump(value["config"], f)


if __name__ == "__main__":
    path_to_consolidated_config = sys.argv[-1]
    create_partial_configs(path_to_consolidated_config)
