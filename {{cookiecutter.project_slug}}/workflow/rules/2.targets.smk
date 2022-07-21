"""
Declare your targets here!
A separate file is ideal if you have lots of target files to create, or need some python logic to determine
the targets to declare. This example shows targets that are dependent on the input file type.
"""

allTargets = []

if inputFile.endswith('.fasta'):
    allTargets.append(outputPrefix + '.fai')
else:
    allTargets.append(outputPrefix + '.touch')
