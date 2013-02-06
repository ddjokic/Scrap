#!/usr/bin/env python
#rename files in python

import os
import datetime
print("Ghost file with name prefix+datetime, without extension will be created. It is safe to delete it.")
print("Note that there are no your data in it.")
dir = raw_input('Enter full directory path: ')
prefix = raw_input('Enter prefix: ')
os.chdir(dir)
allfiles = os.listdir(dir)
for filename in allfiles:
	time = os.path.getmtime(filename)
	v = datetime.datetime.fromtimestamp(time)
	stamp = v.strftime('%Y%m%d-%H%M%S')
	fext=os.path.splitext(filename)
	ext=fext[1]
	os.rename(filename, prefix + stamp +ext)
print("Job Done")