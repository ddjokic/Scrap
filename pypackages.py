#!/usr/bin/env python
#lists all python packages installed
#forked from Clark's Tech Blog - http://www.libertypages.com/clarktech/?p=3571
from pkg_resources import Environment
import sys

c = 0
filename = "pypackages.txt"
fn=open(filename, 'a')
fn.write("Installed python packages:")
for p in Environment():
    c = c + 1
    print "%5d  "%c + p
    fn.write("\n%5d "%c)
    fn.write(p)
fn.close()