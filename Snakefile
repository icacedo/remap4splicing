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
#accs = ['SRR5811858', 'SRR5811862']

# test smaller files
# not paired end, prob better to use actual files

samples = ['SRR23861695', 'SRR23861698']

rule all:
    input:
        expand("{sample}_1.fastq", sample=samples),
        expand("{sample}_2.fastq", sample=samples)

'''
rule all:
    input:
        expand("data/{sample}/{sample}.sra", sample=samples)
'''

rule prefetch:
    params:
        outdir="data/"
    output:
        "data/{sample}/{sample}.sra"
    shell:
        "prefetch {wildcards.sample} -O {params.outdir}"

# need to play with options
# get it to produce a consistent number of files

rule fasterq_dump:
    input:
        "data/{acc}"
    output:
        "{acc}_1.fastq",
        "{acc}_2.fastq"
    shell:
        "fasterq-dump {input}"
