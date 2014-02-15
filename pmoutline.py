#!/usr/bin/env python
'''creates text files out of lines in input text files - poor man outliner, one file for each line, where filename is line of the text in input file - works, sometimes
(c), D.Dj, 2014'''

import os
import string
import datetime
now = datetime.datetime.now()
datet = now.strftime("%d %B, %Y")

#datet= 'Date: '+ str(now.day)+'-'+str(now.month)+'-'+str(now.year)

inp_file = raw_input ("Input filename: ")
path = raw_input("Input full path to folder to store files: ")
fn = open (inp_file, "r")
lines = fn.readlines()
num_lines = len(lines)

os.chdir(path)

for i in range(0, num_lines):
    fn1 = str(lines[i].translate(None, string.punctuation))
    fn = fn1.strip('\n')
    filename = str(fn+'.txt')
    fh = open(filename, 'w')
    fh.write(datet)
    fh.close()
