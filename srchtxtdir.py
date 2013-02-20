#!/usr/bin/env python
#search all text files in a folder for a string
import os

dir = raw_input('Enter full directory path: ')
tsr = raw_input('Enter search string: ')
os.chdir(dir)
allfiles = os.listdir(dir)
for filename in allfiles:
	fext=os.path.splitext(filename)
	ext=fext[1]
	if ext=='.txt':
		with open(filename, 'r') as searchfile:
			for line in searchfile:
				if tsr in line:
					print (fext[0]+fext[1])
					print(line)
				elif tsr.capitalize() in line:
					print (fext[0]+fext[1])
					print(line)
				
	elif ext==".md":
		with open(filename, 'r') as searchfile:
			for line in searchfile:
				if tsr in line:
					print (fext[0]+fext[1])
					print (line)
				elif tsr.capitalize() in line:
					print (fext[0]+fext[1])
					print(line)

print("Done!")    				