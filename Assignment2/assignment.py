import re

rsum = open("regex.txt")
numlist = list()
for line in rsum:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) != 3: continue
    num = int(stuff[0])
    numlist.append(num)
print(sum(numlist))
