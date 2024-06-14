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