### snakemaketools

A Python module with tools to extend snakemake to long pipelines.


### Run snakemake pipeline:
"""shell
snakemake -c1 out/final/1_2.toml
"""
replace 1/2 for the configs you want to use


### create patial configs and save them in the db
"""shell
python long_snake/long_snake/config_parser.py
"""