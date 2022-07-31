"""
{{ cookiecutter.project_name }}
{{ cookiecutter.project_description }}

{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}

This is the main Snakemake pipeline file.
"""

"""CONFIGFILE
Read in the system default configfile is useful to fill in anything the user has accidentally deleted.
Read in other config files that contain immutable settings that the user is NOT allowed to change.
"""
configfile: os.path.join(workflow.basedir, "..", "config", "config.yaml")
configfile: os.path.join(workflow.basedir, "..", "config", "databases.yaml")


"""ADD FUNCTIONS
If your pipeline needs any Python functions, putting them in a separate file keeps things neat.
"""
include: "rules/0.functions.smk"


"""PREFLIGHT CHECKS
Validate your inputs, set up directories, parse your config, etc.
"""
include: "rules/1.preflight.smk"


"""TARGETS
Declare your targets, either here, or in a separate file.
"""
include: "rules/2.targets.smk"


"""RULES
Add rules files with the include directive here, or add rules AFTER rule 'all'.
"""
include: "rules/3.rules.smk"


"""RUN SNAKEMAKE!"""
rule all:
    input:
        allTargets
