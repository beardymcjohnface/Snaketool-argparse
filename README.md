# Snaketool
Cookiecutter profile for making a Snakemake-based bioinformatics tool

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
my_snaketool/
├── bin
│   └── my_snaketool
├── build
│   └── my_snaketool
│       ├── build.sh
│       └── meta.yaml
├── config
│   ├── config.yaml
│   └── databases.yaml
├── test
│   ├── README.md
│   └── test.fasta
├── workflow
│   ├── envs
│   │   └── samtools.yaml
│   ├── rules
│   │   ├── 0.functions.smk
│   │   ├── 1.preflight.smk
│   │   ├── 2.targets.smk
│   │   └── 3.rules.smk
│   ├── scripts
│   │   └── myScript.py
│   ├── install.smk
│   └── run.smk
├── AUTHORS.md
├── CHANGELOG.md
├── LICENCE
├── README.md
├── requirements.txt
└── VERSION


```

The file `bin/my_snaketool` is the convenience launcher (or whatever you called it).
Customise this file to add your own commandline options, help message, utility scripts etc.

The directories `config/` and `workflow/` contain an example Snakemake pipeline that will work
with the example launcher. There are helpful comments throughout these files.

## Installing your tool

For development, install the dependencies in `requirements.txt` with conda.
Then, __softlink__ the convenience launcher to your system PATH, or add the `bin/` to your PATH.
That's it!

## Publishing your tool

For deployment and publishing, add the tool to bioconda or an appropriate channel, 
or even your own channel.

The directory `build/` contains the files needed to build and submit the tool as a conda package.
You __may__ need to tweak the requirements etc. 
You __will__ need to first create a release on GitHub to match the version number in `meta.yaml`
(prepend with a 'v', e.g. GitHub tag is 'v0.1.0' for version '0.1.0'). 
Then, download the 'tar.gz' archive for the tag, calculate the sha256 checksum and paste it the `meta.yaml` file.
Finally, build the conda package and add it to your channel, 
or add it to bioconda-recipes or a suitable channel.
