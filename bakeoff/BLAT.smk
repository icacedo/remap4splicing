# https://genome.ucsc.edu/goldenpath/help/blatSpec.html
# cannot output to sam format

# can't take .fastq as input, must be .fa
# BLATq can accept fastq files
# https://github.com/calacademy-research/BLATq
# blatq is not on conda

# this converts fastq to fa
# sed -n '1~4p;2~4p' fastq > fasta
# -n is required, or it will print more lines than you want

rule all