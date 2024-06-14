import toml
import os

from db import add_config


def load_config(filepath: str):
    return toml.load(filepath)


def create_partial_configs():

    consolidated_config = load_config("dev/consolidated_config.toml")

    for config, value in consolidated_config.items():
        if config == "wildcards":
            continue

        db_config_id = add_config(value["config"])
        file = "{}/{}.{}".format(value["final_folder"], db_config_id,  value["format"])

        # create file if it does not exist
        if not os.path.exists(file):
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, "w") as f:
                toml.dump(value["config"], f)


if __name__ == "__main__":
    create_partial_configs()
