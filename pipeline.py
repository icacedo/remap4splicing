# work on RNA-seq pipeline without Snakemake first

# download SRR4089683 and SRR4089651 from SRA database

'''
gzip -dc SRR4089651.fastq.gz > SRR4089651.fastq
gzip -dc SRR4089683.fastq.gz > SRR4089683.fastq

fastp -i SRR4089651.fastq -o SRR4089651.fq
fastp -i  SRR4089683.fastq -o SRR4089683.fq

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


