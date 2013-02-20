#!/usr/bin/env python

import os
dir = raw_input('Enter full directory path: ')
os.chdir(dir)
allfiles = os.listdir(dir)
#print (allfiles)

filename="000-files_list.txt"
fn=open(filename, 'a')
fn.write(dir)
for fname in allfiles:
	fn.write("\n")
	fn.write(fname)
fn.close()
	