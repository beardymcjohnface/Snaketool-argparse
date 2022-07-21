"""
Add your preflight checks as pure Python code here.
e.g. Configure the run, declare directories, validate the input files etc.
"""


"""CONFIGURATION
parsing the config to variables is not necessary, but it looks neater than typing out config["someParam"] every time.
"""
inputFile = config["infile"]
outputDir = config["outdir"]


"""DIRECTORIES/FILES etc.
Declare some directories for pipeline intermediates and outputs.
"""
stderrDir = os.path.join(outputDir, 'errorLogs')
outputPrefix = os.path.join(outputDir, os.path.basename(inputFile))



"""ONSTART/END/ERROR
Tasks to perform at various stages the start and end of a run.
"""
onstart:
    """Cleanup old log files before starting"""
    if os.path.isdir(stderrDir):
        oldLogs = filter(re.compile(r'.*.log').match, os.listdir(stderrDir))
        for logfile in oldLogs:
            os.unlink(os.path.join(STDERR, logfile))

onsuccess:
    """Print a success message"""
    sys.stderr.write('\n\n{{ cookiecutter.project_name }} finished successfully!\n\n')

onerror:
    """Print an error message"""
    sys.stderr.write('\n\nERROR: {{ cookiecutter.project_name }} failed to finish.\n\n')

