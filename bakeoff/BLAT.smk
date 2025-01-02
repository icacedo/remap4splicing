# https://genome.ucsc.edu/goldenpath/help/blatSpec.html
# cannot output to sam format

# can't take .fastq as input, must be .fa
# BLATq can accept fastq files
# https://github.com/calacademy-research/BLATq
# blatq is not on conda

# this converts fastq to fa
# sed -n '1~4p;2~4p' fastq > fasta
# -n is required, or it will print more lines than you want

# BLAT cannot align paired-end data, each read must be aligned seperately

samples = ['0.1pct.ERR13244179_1', '0.1pct.ERR13244179_2']

rule all:
    input:
        expand('../test_sequences/small_fastq/{sample}.fa', sample=samples)

rule fq2fa:
    input:
        '../test_sequences/small_fastq/{sample}.fastq'
    output:
        '../test_sequences/small_fastq/{sample}.fa'
    shell:
        "sed -n '1~4p;2~4p' {input} | sed 's/@/>/' > {output}"
