#!/usr/bin/env python
#change specified extension of all files in folder

import os
dir = raw_input('Enter full directory path: ')
ext1=raw_input('Enter OLD extension - to be changed: ')
ext2=raw_input('Enter NEW extension: ')
ext3='.'+ext2
ext4='.'+ext1
os.chdir(dir)
allfiles = os.listdir(dir)
for filename in allfiles:
	fext=os.path.splitext(filename)
	fname=fext[0]
	ext=fext[1]
	
	if ext4==ext:
		os.rename(filename, fname+ext3)