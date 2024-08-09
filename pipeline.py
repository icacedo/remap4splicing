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
        file.write(fname)

if not os.path.exists('ind/'):
    os.mkdir('ind/')

# does not include GTF file annotation
if not os.path.exists('ind/Genome'):
    subprocess.run([
        'STAR --runThreadN 2 --runMode genomeGenerate --genomeDir ind/ '
        '--genomeFastaFiles 1pct_elegans.fa'
    ], shell=True)

filesin = ''
fq_files = os.listdir('fastq/')
for file in fq_files:
    if file != fq_files[-1]:
        filesin += f'../fastq/{file},'
    else:
        filesin += f'../fastq/{file}'

if not os.path.exists('Sout/'):
    os.mkdir('Sout/')

subprocess.run([
    f'STAR --runThreadN 15 --genomeDir ../ind/ --readFilesIn {filesin}'
], cwd='Sout/', shell=True)


#STAR --runThreadN 2 --genomeDir ind/ --readFilesIn SRR4089683.fastq,SRR4089651.fastq

#samtools view -S -b Aligned.out.sam > Aligned.out.bam
#samtools sort -o Aligned.out.sorted.bam Aligned.out.bam

# use 2-pass mapping to find novel splice junctions
# https://www.reneshbedre.com/blog/star-aligner.html
# need gtf from gff
# https://github.com/NBISweden/AGAT













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


