"""
Add your rules! Split them over multiple files if you have lots.
"""

rule copyInfile:
    """Copy the input file to the output directory"""
    input:
        inputFile
    output:
        outputPrefix
    shell:
        """cp {input} {output}"""

rule samtoolsFaidx:
    """Run samtools faidx on a fasta input file"""
    input:
        outputPrefix
    output:
        outputPrefix + '.fai'
    conda:
        os.path.join('..','envs','samtools.yaml')
    log:
        os.path.join(stderrDir, 'samtoolsFaidx.log')
    shell:
        """samtools faidx {input} -o {output}"""

rule touchInput:
    """Touch a non-fasta input file"""
    input:
        outputPrefix
    output:
        touch(outputPrefix + '.touch')
    log:
        os.path.join(stderrDir, 'touchInput.log')
    script:
        os.path.join('../', 'scripts', 'myScript.py')
