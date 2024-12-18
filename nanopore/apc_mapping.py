import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('txt')
parser.add_argument('apc_dir')

args = parser.parse_args()

'''
from itertools import groupby

# copy pasted from google
def query_len(cigar_string):
    """
    Given a CIGAR string, return the number of bases consumed from the
    query sequence.
    """
    read_consuming_ops = ("M", "I", "S", "=", "X")
    result = 0
    cig_iter = groupby(cigar_string, lambda chr: chr.isdigit())
    for _, length_digits in cig_iter:
        length = int(''.join(length_digits))
        op = next(next(cig_iter)[1])
        if op in read_consuming_ops:
            result += length
    return result
'''

# need to get total length of alignment including gaps/indels
# from CIGAR string
# 4S means 4 bases were soft clipped
# bases not part of the alignment
# see page 8 of sam manual, see what consumes query/sequence
# sum of lengths of M/I/S/=/X = length of SEQ
# just getting the length of the sequence is way easier...

mapped = {}
with open(args.txt) as fp:
    for line in fp.readlines():
        line = line.rstrip()
        line = line.split('\t')
        if line[1] == '0':
            rid = line[0]
            pos = line[3]
            slen = len(line[9])
            mapped[rid] = [int(pos), slen]

#for i in mapped:
#    print(i, mapped[i])

genes = {}
for item in os.listdir(args.apc_dir):
    if item.endswith('fa'):
        with open(f'{args.apc_dir}{item}') as fp:
            gid = ''
            seq = ''
            for line in fp.readlines():
                line = line.rstrip()
                if line.startswith('>'):
                    gid = line
                else:
                    seq += line
            genes[gid] = seq

#print(genes)

# if reads overlap with at least one base: assign to gene
# find a way to put this into jbrowse

# II:3243554-3244269
#




