import re
import sys
import os

regex_sum = open(regex_sum.txt)
numlist = list()
for line in regex_sum:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) =! 1: continue
    for num in stuff:
        numlist.append(int(num))