# Snaketool
Cookiecutter profile for making a Snakemake-based bioinformatics tool

__See also a better, pip installable version using Click: [Snaketool-lite](https://github.com/beardymcjohnface/Snaketool-lite)__

## Motivation

Writing reliable command line tools requires a lot of boilerplate to ensure input and generated
files are valid, catch errors with subprocesses, log stderr messages etc. It's very time-consuming and annoying.
Snakemake does a lot of heavy lifting in this regard and is an obvious alternative to a command line tool.

While Snakemake pipelines are excellent, cloning a pipeline repo every time you want to run an analysis is also annoying.
So too is manually punching in the full path to a Snakefile somewhere on your system,
as well as copying and manually updating the config file for your analysis.

Building a Snakemake pipeline with a convenience launcher offers the best of both worlds:
- Developing command line applications is quicker and easier
- Installing, running, and rerunning is easier and more convenient
- You can have subcommands for utility scripts and Snakefiles
- You can trick NextFlow users into running Snakemake
- Your pipelines have help messages!

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

## How the launcher works

The launcher first copies the default config file to the working directory which will allow the user to cusomise their
config if they wish. The launcher reads in this config file and combines it with command-line arguments to pass on to 
Snakemake. In this example it only has two options to pass: `--input` and `--output`. The Launcher writes a new config 
file in the output directory which will be passed to Snakemake. The launcher uses the rest of the command line arguments 
to launch Snakemake. Most of the command line arguments are boilerplate for running Snakemake and do not require much if
any customisation.

## Installing and testing your tool

For development, cd to your Snaketool directory and install with pip:

```shell
cd snaketool/
pip install -e .
snaketool -h
```

Test run template's inbuild test:

```shell
my_snaketool test
```

## Publishing your tool

Add your tool to pip and bioconda.
Instructions TBA, watch this space!

