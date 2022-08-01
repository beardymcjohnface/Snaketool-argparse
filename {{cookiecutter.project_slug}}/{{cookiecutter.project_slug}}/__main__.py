#!/usr/bin/env python3

"""
{{ cookiecutter.project_description }}

{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}
"""

import argparse
import sys
import os
import subprocess
import yaml
from shutil import copyfile
from time import localtime, strftime


"""MISC FUNCTIONS
You shouldn't need to tweak these much if at all
- Set a different default system config file in copy_config() if you need to"""


def snake_base(rel_path):
    return os.path.join(os.path.dirname(__file__), rel_path)


def print_version():
    with open(snake_base('{{cookiecutter.project_slug}}.VERSION'), 'r') as f:
        version = f.readline()
    sys.stderr.write('{{cookiecutter.project_name}} version ' + version + '\n')


def msg(err_message):
    tstamp = strftime('[%Y:%m:%d %H:%M:%S] ', localtime())
    sys.stderr.write(tstamp + err_message + '\n')


def msg_box(splash, errmsg=None):
    msg('-' * (len(splash) + 4))
    msg(f'| {splash} |')
    msg(('-' * (len(splash) + 4)))
    if errmsg:
        sys.stderr.write('\n' + errmsg + '\n')


def copy_config(local_config, system_config=snake_base(os.path.join('config', 'config.yaml'))):
    if not os.path.isfile(local_config):
        msg(f'Copying system default config to {local_config}')
        copyfile(system_config, local_config)
    else:
        msg(f'Config file {local_config} already exists. Using existing config file.')


def read_config(file):
    with open(file, 'r') as stream:
        _config = yaml.safe_load(stream)
    return _config


def write_config(_config, file):
    msg(f'Writing runtime config file to {file}')
    with open(file, 'w') as stream:
        yaml.dump(_config, stream)


"""Customise your argparse arguments!"""


def parseArgs():
    print_version()
    snakeDefaults = ['--rerun-incomplete', '--printshellcmds ', '--nolock ', '--show-failed-logs ']


    """Customise your help message!"""


    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=("\n"
                     "Subcommands:\n"
                     "    run         Run {{ cookiecutter.project_name }}\n"
                     "    install     Download and install the databases or dependencies\n"
                     "    config      Copy the default configfile to the current directory\n"
                     "    test        Run the test dataset\n"
                     "\n"),
        epilog=  ("Example usage: \n"
                 "To Run {{ cookiecutter.project_name }}:\n"
                 "{{ cookiecutter.project_slug }} run --infile file\n"
                 "\n"
                 "Run on a cluster:\n"
                 "{{ cookiecutter.project_slug }} run --infile file --profile slurm\n"
                 "\n"
                 "Copy the default config to customise your analysis:\n"
                 "{{ cookiecutter.project_slug }} config \n"
                 "\n"
                 "Install databases/dependencies:\n"
                 "{{ cookiecutter.project_slug }} install \n"
                 "\n"
                 "Run the test dataset:\n"
                 "{{ cookiecutter.project_slug }} test \n"
                 "\n")
    )


    """COMMAND LINE OPTIONS
    --infile and --outdir are simply passed as config options verbatim to Snakemake.
    You should keep --profile, --threads, --configfile, and --snake to make the most out of Snakemake.
    --snake-default lets the user override the default Snakemake options if they're feeling brave."""


    parser.add_argument('command', choices=['run', 'install', 'config', 'test'])
    parser.add_argument('--infile', help='Input file required for {{ cookiecutter.project_slug }}')
    parser.add_argument('--outdir', help='Directory to write the output files', default='output_{{ cookiecutter.project_slug }}')
    parser.add_argument('--profile', help='Snakemake profile for use on HPC cluster')
    parser.add_argument('--threads', help='Number of threads to use (ignored if using --profile)', default='8')
    parser.add_argument('--configfile',
                        help='Specify a config file. (default {{ cookiecutter.project_slug }}.config.yaml)',
                        default='{{ cookiecutter.project_slug }}.config.yaml')
    parser.add_argument('--use-conda', action='store_const', const=True, default=True, help='Use conda for Snakemake rules', dest='use_conda')
    parser.add_argument('--no-use-conda', help='Do not use conda for Snakemake rules', action='store_const', const=True, dest='use_conda')
    parser.add_argument('--conda-frontend', choices=['mamba', 'conda'], dest='conda_frontend',
                         default='{{cookiecutter.conda_frontend}}', help='Specify Conda frontend')
    parser.add_argument('--conda-prefix', default=snake_base(os.path.join('workflow', 'conda')),
                        dest='conda_prefix', help='Custom conda env directory')
    parser.add_argument('--snake-default',
                        help=f'Commandline options passed by default to Snakemake. (default {" ".join(snakeDefaults)})',
                        default=snakeDefaults)
    parser.add_argument('--snake',
                        help='Pass additional commands to Snakemake e.g. --snake=--dry-run --snake=--forceall',
                        action='append')
    args = parser.parse_args()
    return args


def run_snakemake(configfile=None, snakefile_path=None, merge_config={}, profile=None, threads=1, use_conda=False,
                  conda_frontend=None, conda_prefix=None, outdir='{{cookiecutter.project_slug}}.out',
                  snake_default_args=None, snake_extra=[]):
    """Run a Snakefile"""
    snake_command = f'snakemake -s {snakefile_path} '

    # if using a configfile
    if configfile:
        # copy sys default config if needed
        copy_config(configfile)

        # read the config
        snake_config = read_config(configfile)

        # merge in command line config if provided
        if merge_config:
            snake_config.update(merge_config)

        # create runtime config file for Snakemake execution
        runtime_config = os.path.join(outdir, '{{cookiecutter.project_slug}}.config.yaml')
        if not os.path.exists(os.path.normpath(outdir)):
            os.makedirs(os.path.normpath(outdir))
        write_config(snake_config, runtime_config)
        snake_command = snake_command + f'--configfile {runtime_config} '

        # display the runtime configuration
        msg_box('Runtime config', errmsg=yaml.dump(snake_config, Dumper=yaml.Dumper))

    # either use -j [threads] or --profile [profile]
    if profile:
        snake_command = snake_command + f'--profile {profile} '
    else:
        snake_command = snake_command + f'-j {threads} '

    # add conda args if using conda
    if use_conda:
        snake_command = snake_command + f'--use-conda --conda-frontend {conda_frontend} --conda-prefix {conda_prefix} '

    # add snakemake default args
    if snake_default_args:
        snake_command = snake_command + ' '.join(s for s in snake_default_args) + ' '

    # add any additional snakemake commands
    if snake_extra:
        snake_command = snake_command + ' '.join(s for s in snake_extra)

    # Run Snakemake!!!
    msg_box('Snakemake command', errmsg=snake_command)
    if not subprocess.run(snake_command.split()).returncode == 0:
        msg('Error: Snakemake failed')
        sys.exit(1)
    else:
        msg('Snakemake finished successfully')
    return 0


def install(args):
    """The install function. This will run the install.smk snakemake pipeline."""
    run_snakemake(
        snakefile_path=snake_base(os.path.join('workflow', 'install.smk')),
        configfile=args.configfile,
        threads=args.threads,
        profile=args.profile)


def run(args):
    """Run {{cookiecutter.project_name}}!"""
    merge_config = {'infile': args.infile}

    # run!
    run_snakemake(
        snakefile_path=snake_base(os.path.join('workflow', 'run.smk')),
        configfile=args.configfile,
        outdir=args.outdir,
        merge_config=merge_config,
        threads=args.threads,
        profile=args.profile,
        use_conda=args.use_conda,
        conda_frontend=args.conda_frontend,
        conda_prefix=args.conda_prefix,
        snake_default_args=args.snake_default,
        snake_extra=args.snake,
    )


def testRun(args):
    """Run the test dataset"""
    msg('Running the test dataset')
    args.infile = os.path.normpath(snake_base(os.path.join('workflow', 'test', 'test.fasta')))
    run(args)
    return None


def copyConfig(args):
    """Copy the sys default config and exit"""
    copy_config(args.configfile)
    return None


def main():
    commands = {'install': install, 'run': run, 'config': copyConfig, 'test': testRun}
    args = parseArgs()
    commands[args.command](args)


if __name__ == '__main__':
    main()
