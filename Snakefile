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


def parser(wildcards):
    ...
    return {'a': 121}

rule make_fourth:
    output:
        "P/fourth/{something}"
    input:
        unpack(parser)
    run:
        pass


rule complicated_rule:
    input:
        "P/first/{very_long_input_1}",
        "P/second/{very_long_input_2}",
        "P/third/{very_long_input_3}",
        "P/fourth/{very_long_input_4}",
    output:
        "P/complicated_rule/{output}"
