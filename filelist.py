#!/usr/bin/env python
'''list files in filder and all sub-folders and writing result
	in 000-file_list.txt, located in folder examined.
	feel free to modify, as you see fits
	(c) 2014, D. Djokic. No warranties'''
	
import os

path = raw_input ("Enter full directory path: ")
os.chdir(path)
filename = "000-file_list.txt"
fn = open(filename, "w")

for root, dirs, files in os.walk (path, topdown=True):
	fn.write (str(root))
	fn.write ("\n")
	fn.write (str(dirs))
	
	for file in files:
		
		fn.write("\n")
		fn.write(str(file))

fn.close()
