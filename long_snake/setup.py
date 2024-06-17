# This Python file uses the following encoding: utf-8
import glob

from setuptools import find_packages, setup

setup(
    name="long_snake",
    packages=find_packages(),
    version="0.0.1",
    description="Tools for working with long Snakemake pipelines.",
    long_description="Extend Snakemake to work nicely with longer pipelines.",
    author="Mateusz Krzysztof Łącki & Thilo Schild",
    author_email="matteo.lacki@gmail.com",
    url="https://github.com/MatteoLacki/LongSnake.git",
    keywords=["bioinformatics", "pipelines"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    install_requires=["snakemake", "toml", "pony"],
    scripts=glob.glob("tools/*.py"),
)
