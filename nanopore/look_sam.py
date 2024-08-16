import sys

sam = sys.argv[1]

def is_num(s):

    try:
        return int(s)
    except ValueError:
        return None

with open(sam, 'r') as fp:
    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('@'): continue
        line = line.split('\t')
        cigar = line[5]
        seq = line[9]
        total = 0
        for s in cigar:
            val = is_num(s)
            if isinstance(val, int) == True:
                total += val
        print(total)
        print(len(seq))
        break