# i am not sure of a way to integrate quality control into an automated pipeline
# use this script to run fastqc on all the samples i want to use
# filter samples by hand to run with the snakemake pipeline

import argparse
import os
import subprocess

parser = argparse.ArgumentParser(
    description="Run fastqc on selected fastq files")
parser.add_argument("fastq_dir", help="directory with fastq files")

args = parser.parse_args()

if os.path.exists("fqc/") == False:
    os.makedirs("fqc/")

# need to activate proper conda environment
for item in os.listdir(args.fastq_dir):
    subprocess.run(f"fastqc {args.fastq_dir}{item} -o fqc/", shell=True)