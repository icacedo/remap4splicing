import argparse

parser = argparse.ArgumentParser()

parser.add_argument('txt')

args = parser.parse_args()

with open(args.txt) as fp:
    for line in fp.readlines():
        line = line.rstrip()
        line = line.split('\t')
        print(line)
        for item in line:
            print(item)
        break