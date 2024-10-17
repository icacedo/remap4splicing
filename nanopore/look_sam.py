import sys

sam = sys.argv[1]

flag_counts = {}
with open(sam, 'r') as fp:
    for line in fp.readlines():
        if line.startswith('@'): continue
        line = line.rstrip()
        line = line.split()
        if line[1] not in flag_counts:
            flag_counts[line[1]] = 1
        else:
            flag_counts[line[1]] += 1
        #if line[1] == '272':
            #print(line)
print(flag_counts)