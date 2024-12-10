import argparse
import gzip

parser = argparse.ArgumentParser()
parser.add_argument("filtered_sam", type=str, metavar='<file>', 
    help="sam file with unammped reads removed")
parser.add_argument("fasta_r1", type=str, metavar='<file>',
    help="fasta or fastq file with unfiltered r1 reads")
parser.add_argument("fasta_r2", type=str, metavar='<file>',
    help="fasta or fastq file with unfiltered r2 reads")

args = parser.parse_args()

def get_reads(fasta):

    reads = {}
    count = 0
    if fasta.endswith('gz'): 
        with gzip.open(fasta, 'rt') as fp:
            for line in fp.readlines():
                line = line.rstrip().split(' ')
                if count == 4: count = 0
                if count == 0:
                    rid = line[0][1:]
                    reads[rid] = [line]
                else:
                    reads[rid].append(line)
                count += 1
    
    return reads
            
r1_reads = get_reads(args.fasta_r1)
r2_reads = get_reads(args.fasta_r2)

read_ids = []
with open(args.filtered_sam, 'rt') as fp:
    for line in fp.readlines():
        if line.startswith('@'): continue
        line = line.rstrip().split('\t')
        read_ids.append(line[0])

for i in read_ids:
    print(i)
    break

print('#####')

# now need to rewrite fasta files with only aligned reads
# need both paired reads in seperate fasta files

for rid in read_ids:
    print(r1_reads[rid])