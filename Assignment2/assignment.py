import re

rsum = open("regex.txt")
numlist = []

for line in rsum:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    if len(stuff) < 1: continue
    for i in range(len(stuff)):
        num = float(stuff[i])
        numlist.append(num)
print(sum(numlist))
