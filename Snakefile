rule copy_step_0_config:
    input:
        "partial_configs/step_0/{config}.toml"
    output:
        "out/step_0/{config}.toml"
    shell:
        "cp {input} {output}"



rule copy_step_1_config:
    input:
        "partial_configs/step_1/{config}.toml"
    output:
        "out/step_1/{config}.toml"
    shell:
        "cp {input} {output}"



rule do_something_with_results:
    input:
        "out/step_0/{config0}.toml",
        "out/step_1/{config1}.toml",
    output:
        "out/final/{config0}_{config1}.toml"
    shell:
        "cat {input} > {output}"


rule turn_toml_into_json:
    input:
        "{path}.toml"
    output:
        "{path}.json"
    run:
        import tomllib
        import json
        from pprint import pprint

        with open(input, "rb") as _in, open(output, "w") as _out:
            config = tomllib.load(_in)
            pprint(config)
            json.dump(config, _out)
