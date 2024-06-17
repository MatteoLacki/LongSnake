* Write a script that:
    1. reads in a consolidated config
    2. parses it into constituent configs
    3. checks if constituent configs are in the DB
        * if no, create an entry and save the config under partial_configs/{id}.toml
        * else, nothing
    4. runs snakemake with proper subconfig names in the output.
        * do_something_with_results rule must be used.

* How to deal with potentially many simultaneous queries?
    * sqlite3 setting

Help:
https://editor.ponyorm.com/user/MatteoLacki/snakemake/sqlite




configs:

1.toml # config for rule 1.
# stored under configs/rule1/1.toml

2.toml
3.toml

# forward functions:

def rule_1( config: str, necessary: str ):
    return f"P/rule1/[{config}][{necassary}].out" # AKA the long path string

# a pipeline: a fuction defining longer path templates:

def create_path_templates(
    wildcards: dict,
    forward_rules: dict,
    path_templates: dict = {},
) -> dict:
    config_for_rule_1

    path_templates.precursor_clustering_script = Path(
        "configs/clustering/{precursor_clusterer}/{precursor_clusterer_version}/{precursor_clusterer_version}.py"
    )


# a rule among some rule files .smk

rule 1: # the old way
    output:
        "P/rule1/{config_file}_{necessary}.out"
    input:
        "configs/rule1/{config_file}.toml"
        "something/{necessary}.vip"

rule 1: # the old way
    output:
        "P/rule1/{to_be_parsed}.out"
    input:
        encoder.parse(wildcards)

Right now:
to_be_decompressed -> 
"P/rule1/[configs/rule1/1.toml][something/wildcard_filled_necessary.vip]"

to_be_parsed -> id in a DB -> under this DB entry:


to_be_parsed 

rule W:
    output:
        "/P/W/{file}"
    input:
        unpack(encoder.parse)# -> 
        # encoder.parse(wildcards) : a function parsing out inputs.

######## THE FINAL FINAL TODO:

1. Make a pipeline of the following form:

# all this into Snakefile

def rule_1(config: str) -> str:
    return "P/rule_1/[config].out1"


def rule_2(rule_1_out: str, config: str) -> str:
    assert Path(rule_1_out).suffix == ".out1"
    return (
        "P/rule_2/[rule_1_out][config].out2",
        "P/rule_2/[rule_1_out][config].toml",
    )


def create_path_templates(
    wildcards: dict,
    forward_rules: dict,
    path_templates: dict = {},
) -> dict:
    path_templates["config_for_rule_1"] = "partial_config/rule1/{config_for_rule_1}"
    path_templates["output_of_rule_1"] = rule_1(path_templates["config_for_rule_1"])

    path_templates["config_for_rule_2"] = "partial_config/rule2/{config_for_rule_2}"
    path_templates["output_of_rule_2"], path_templates["auto_gen_config_for_rule_1"]  = rule_2(output_of_rule_1, path_templates["config_for_rule_2"])

    path_templates["output_of_rule_1_after_rule_2"] = rule_1(path_templates["auto_gen_config_for_rule_1"])
    # path_templates["output_of_rule_1"] = rule_1(path_templates["auto_gen_config_for_rule_1"]) # also possible: this must work as well

    ruturn path_templates

def fill_path_templates_with_wildcards(paths_templates, wildcards) -> dict:
    return {
        name: Path(str(path_template).format(**wildcards))
        for name, path_template in path_templates.items()
    }

wildcards_dict = {
    "config_for_rule_1": "1.toml",
    "config_for_rule_2": "2.toml",
}

DB = ??? # help

def short_name_from_DB( name, filled_path ):
    """ 
    Check if the filled_path is in the DB and return its ID or create and return it.
    """

def create_entries_in_db_whenever_thats_necessary(filled_path_templates) -> dict:
    return {
        name: short_name_from_DB( name, filled_path )
        for name, filled_path in filled_path_templates.items()
    }


def give_inputs(wildcards):
    path_templates = create_path_templates(wildcards_dict)
    filled_path_templates = fill_path_templates_with_wildcards(path_templates, wildcards)
    filled_path_templates_as_short_output_file_ids = create_entries_in_db_whenever_thats_necessary(filled_path_templates)
    return filled_path_templates


rule run_pipeline:
    output:
        directory("out/final_outcomes")
    input:
        give_inputs


