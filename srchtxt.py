#!/usr/bin/env python
# copied from net
fid=raw_input("Input file to search: ")
tsr=raw_input("Input search phrase: ")
with open(fid, 'r') as searchfile:
    for line in searchfile:
        if tsr in line:
            print line