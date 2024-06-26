'''
Using Illumina HiSeq 2000 reads from this paper:
The substrates of Nonsense-Mediated mRNA Decay in Caenorhabditis elegans, 
Muir et. al., 2018
GEO database accession number GSE100929
wild type (N2)
smg-1(r910)
smg-1(r910)smg-2(r915)
GSM2696743-GSM2696757
SRX2990418
    SRR5811858-SRR5811862
+ 15 samples
fastq files are about x7 the size of accession
fasterq-dump needs temporary space about x1.5 of final fastq files
space needed during conversion is about x17 the size of the accession
'''
#samples = ['SRR5811858', 'SRR5811862']

# test smaller files
# single end RNA-seq
# single cell blastomere sample from C. elegans
samples = ['SRR4089683', 'SRR4089651']

rule all:
    input:
        expand("fastq/{sample}.fastq", sample=samples)

rule prefetch:
    params:
        outdir="sra/"
    output:
        directory("sra/{sample}")
    shell:
        "prefetch {wildcards.sample} -O {params.outdir}"

# if reads are paired-end, will output two fastq files
# this workflow will only work for single-end reads
rule fasterq_dump:
    params:
        outdir="fastq/"
    input:
        directory("sra/{sample}")
    output:
        "fastq/{sample}.fastq"
    shell:
        "fasterq-dump {input} --outdir {params.outdir}"


