'''
Using Illumina HiSeq 2000 reads from this paper:
The substrates of Nonsense-Mediated mRNA Decay in Caenorhabditis elegans, 
Muir et. al., 2018
GEO database accession number GSE100929

SRR5811887, sample S1ln3, smg-1(r910) input 3
SRR5811906, sample S2ln1, smg-1(r910) smg-2(r915) input 2
SRR5811868, sample N2ln3, N2 input 3

Work on RNA-seq pipeline without snakemake first
Translate to Snakemake later
'''


import subprocess
import os

samples = ['SRR5811887', 'SRR5811906', 'SRR5811868']

# download test samples
if not os.path.exists('data/'):
    os.mkdir('data/')

for sample in samples:
    if os.path.isfile(f'data/{sample}/{sample}.sra'): continue
    subprocess.run([f'prefetch {sample} -O data/'], shell=True)

if not os.path.exists('fastq/'):
    os.mkdir('fastq/')

for sample in samples:
    if os.path.isfile(f'fastq/{sample}.fastq'): continue
    subprocess.run([f'fasterq-dump data/{sample} --outdir fastq/'], shell=True)

# ln -s 1% genome build from datacore2024/
    
# create text input files for rmats
c = 0
for fname in os.listdir('fastq/'):
    c += 1
    if os.path.isfile(f's{c}'): continue
    with open(f's{c}.txt', 'w') as file:
        file.write(f'fastq/{fname}')

if not os.path.exists('ind/'):
    os.mkdir('ind/')

# does not include GTF file annotation
if not os.path.exists('ind/Genome'):
    subprocess.run([
        'STAR --runThreadN 2 --runMode genomeGenerate --genomeDir ind/ '
        #'--genomeFastaFiles 1pct_elegans.fa'
        '--genomeFastaFiles c_elegans.PRJNA13758.WS282.genomic.fa'
    ], shell=True)

filesin = {}
fq_files = os.listdir('fastq/')
for file in fq_files:
    id = file.split('.')[0]
    filesin[id] = f'../fastq/{file}'

for id in filesin:
    if not os.path.exists(f'Sout_{id}/'):
        os.mkdir(f'Sout_{id}/')

# this step takes a while
# maybe make the input fastas shorter
for id in filesin:
    if not os.path.exists(f'Sout_{id}/Aligned.out.sam'):
        subprocess.run([
            f'STAR --runThreadN 15 --genomeDir ../ind/ '
            f'--readFilesIn {filesin[id]}'
        ], cwd=f'Sout_{id}/', shell=True)

for id in filesin:
    if not os.path.exists(f'Sout_{id}/Aligned.out.sorted.bam'):
        subprocess.run([
            'samtools view -S -b Aligned.out.sam > Aligned.out.bam &&'
            'samtools sort -o Aligned.out.sorted.bam Aligned.out.bam'
        ], cwd=f'Sout_{id}', shell=True)

# gtf file is required for rmats
# gffread 1pc_elegans.gff3 -T -o- | more > 1.gtf

# rmats.py --s1 s1.txt --s2 s2.txt --gtf 1.gtf --bi ind/ -t single
# --readLength 101 --od rmats_out/ --tmp rmats_tmp/
# --nthread
# --novelSS to find novel splice sites, default is off
# consider setting --anchorLength, default is 1 which is probably 
# way to low
# need to specify to run stats with
# --task stat

# can i create bam files from long read sequencing data and use that in rmats?

# need to create two bam files for each sample group
# this error comes from STAR
# rmats is trying to run STAR but can't
# EXITING because of FATAL ERROR: could not open genome file

# use 2-pass mapping to find novel splice junctions
# https://www.reneshbedre.com/blog/star-aligner.html
# need gtf from gff
# https://github.com/NBISweden/AGAT

# make bam.txt files for rmats

# rmats did not find any hits with the 1 pct genome
# try full length
# wget PRJNA13758 WS282 genomic.fa.gz
# wget PRJNA13758 WS282 annotations.gff3.gz









'''


get 1% genome build from datacore2024/ with ln -s

make directory to store STAR index files
mkdir ind/

does not include GTF file annotation
STAR --runThreadN 2 --runMode genomeGenerate --genomeDir ind/ --genomeFastaFiles 1pct_elegans.fa

STAR --runThreadN 2 --genomeDir ind/ --readFilesIn SRR4089683.fastq,SRR4089651.fastq

samtools view -S -b Aligned.out.sam > Aligned.out.bam
samtools sort -o Aligned.out.sorted.bam Aligned.out.bam

need to follow the rmats tutorial
https://github.com/Xinglab/rmats-turbo/blob/v4.3.0/README.md

run rmats with conda in the terminal using rmats.py



'''


