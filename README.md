# Snaketool
Cookiecutter profile for making a Snakemake-based bioinformatics tool

__See also a better, pip installable version using Click: [Snaketool-lite](https://github.com/beardymcjohnface/Snaketool-lite)__

## Motivation

Snakemake pipelines are excellent.
However, cloning a pipeline repo every time you want to run an analysis is annoying.
So too is manually punching in the full path to a Snakefile somewhere on your system,
as well as copying and manually updating the config file for your analysis.

Running a Snakemake pipeline via a convenience launcher offers many advantages:
- You can publish it as normal-looking bioinformatics tool and trick NextFlow users into using Snakemake
- It's easier to install, use, and reuse
- You can add subcommands for utility scripts and Snakefiles
- You can write a help message!

## Who is this for?

People who are already familiar with Snakemake and want to create a Snakemake-powered commandline 
tool--or fancier pipelines.

## Usage

To create a new tool from this template, use Cookiecutter and follow the prompts.

```shell
cookiecutter https://github.com/beardymcjohnface/Snaketool.git
```

And here's what you get:

```text
snaketool/
├── AUTHORS.md
├── CHANGELOG.md
├── README.md
├── setup.py
└── snaketool
    ├── config
    │   ├── config.yaml
    │   └── databases.yaml
    ├── __init__.py
    ├── __main__.py
    ├── snaketool.LICENSE
    ├── snaketool.VERSION
    └── workflow
        ├── envs
        │   └── samtools.yaml
        ├── install.smk
        ├── rules
        │   ├── 0.functions.smk
        │   ├── 1.preflight.smk
        │   ├── 2.targets.smk
        │   └── 3.rules.smk
        ├── run.smk
        ├── scripts
        │   └── myScript.py
        └── test
            ├── README.md
            └── test.fasta

```

The file `__main__.py` is the entry point.
Once installed with pip in this example it will be accessible on command line as `snaketool`.
Customise this file to add your own commandline options, help message, utility scripts etc.

The directories `config/` and `workflow/` contain an example Snakemake pipeline that will work with the example launcher.
Feel free to adapt the workflow, or delete and remake.

## Installing and testing your tool

For development, cd to your Snaketool directory and install with pip:

```shell
cd snaketool/
pip install -e .
snaketool -h
```

## Publishing your tool

Add your tool to pip and bioconda.
Instructions TBA, watch this space!

