'''
from Roach et. al. 2020, full-length C. elegans transcriptome
nanopore sequencing reads can be found at
European Nucleotide Archive
accession number PRJEB31791
for testing, get fastq from run ERR3245465
'''

import subprocess
import os

if not os.path.exists('data/'):
    os.mkdir('data/')

if not os.path.exists('data/ERR3245465'):
    subprocess.run([
        'wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR324/005/ERR3245465/'
        'ERR3245465.fastq.gz'
    ], shell=True)

# minimap2 says for long reads CIGAR strings may not be converted to BAM
# https://en.wikipedia.org/wiki/Phred_quality_score

# to test rmats, need another sample to compare
# can test how splicing changes between replicates?
# seems to be a lot of low quality phred scores in the sam file
# gather all reads that map to the same place and aggregate phred scores?

# STAR and minimap2 are splice aware aligners, both can be used for long reads

# minknow and guppy for nanopore base calling

# rm -Rf ~/.vscode-server/

# https://docs.tinybio.cloud/docs/minimap2-tutorial
# minimap2 can use fasta, fastq, sam/bam

# information on SAM file format
# https://samtools.github.io/hts-specs/SAMv1.pdf
# https://www.metagenomics.wiki/tools/samtools/bam-sam-file-format
# 2048 is the supplementary alignment?

# this seems like a good explanation
# https://cloud.wikis.utexas.edu/wiki/spaces/CoreNGSTools/pages/54068983/Filtering+with+SAMTools

# https://cmdcolin.github.io/posts/2022-02-06-sv-sam
# cigar string gives info on alignment
# 50M means 50 matched
# 50I means 50 inserted
# 5D means 5 deleted
# 500S means 500 soft clipped
# will have the same readname, QNAME
# SA supplementary alignment tag may say where the softclipped sequences mapped 
# https://samtools.github.io/hts-specs/SAMtags.pdf
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8652018/