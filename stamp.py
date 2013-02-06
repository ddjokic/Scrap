#!/usr/bin/env python
#rename files in python

import os
import datetime
print("Adding date and timestamp to filename")
dir = raw_input("Enter full directory path: ")
os.chdir(dir)
allfiles = os.listdir(dir)
for filename in allfiles:
	time = os.path.getmtime(filename)
	v = datetime.datetime.fromtimestamp(time)
	stamp = v.strftime('%Y%m%d-%H%M%S')
	fext=os.path.splitext(filename)
	fnm=fext[0]
	ext=fext[1]
	os.rename(filename, fnm + stamp +ext)
print("Job Done")