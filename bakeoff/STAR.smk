# modularize snakemake workflows
# create a snakefile for each alignment program
# https://snakemake.readthedocs.io/en/v3.9.1/snakefiles/modularization.html
# https://hbctraining.github.io/Intro-to-rnaseq-hpc-O2/lessons/03_alignment.html

import os

if os.cpu_count() <= 2:
    cores = 1
else:
    cores = os.cpu_count() - 2

rule index:
    input:
        "../test_sequences/genome/1pct_elegans.fa"
    output:
        directory("gen/")
    shell:
        """
        STAR --runThreadN {cores} --runMode genomeGenerate --genomeDir {output} \
        --genomeFastaFiles {input} 
        """

# STAR isn't using multiple threads when specified?
rule align:
    input:
        directory("gen/")
    output:
