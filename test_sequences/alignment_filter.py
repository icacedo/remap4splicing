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

    if fasta.endswith('gz'): 
        with gzip.open(fasta, 'rt') as fp:
            content = fp.read().rstrip()
            content = content.split('\n')
    else:
        with open(fasta, 'rt') as fp:
            content = fp.read().rstrip()
            content = content.split('\n')
    
    '''
    for line in content:
        print(line)
        line = line.rstrip().split(' ')
        if count == 4: count = 0
        if count == 0:
            rid = line[0][1:]
            reads[rid] = [line]
        else:
            reads[rid].append(line)
            count += 1
    '''
    reads = {}
    rid = ''
    count = 0
    for line in content:
        if count == 0:
            rid = line.split(' ')[0][1:]
            reads[rid] = [line]
            count += 1
        else:
            reads[rid].append(line)
            count += 1
        if count == 4: count = 0

    return reads

# should i write something to verify each entry has the correct info?
# i.e. the ID is always the ID, the sequence is always the sequence...            
r1_reads = get_reads(args.fasta_r1)
r2_reads = get_reads(args.fasta_r2)

read_ids = []
with open(args.filtered_sam, 'rt') as fp:
    for line in fp.readlines():
        if line.startswith('@'): continue
        line = line.rstrip().split('\t')
        read_ids.append(line[0])

# now need to rewrite fasta files with only aligned reads
# need both paired reads in seperate fasta files


with open('new.fastq', 'w') as file:
    for rid in read_ids:
        for line in r1_reads[rid]:
            file.write(f'{line}\n')


