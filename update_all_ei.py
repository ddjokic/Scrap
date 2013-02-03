#!/usr/bin/env python
#credits: http://www.snipplr.com/view.php?codeview&id=56085 and author
from setuptools.command.easy_install import main as install
from pkg_resources import Environment, working_set
import sys

#Packages managed by setuptools
plist = [dist.key for dist in working_set]

def autoUp():
    for p in Environment():
        try:
            install(['-U', '-v']+[p])
        except:
            print "Update of %s failed!"%p
        print "Done!"

def stepUp():
    for p in Environment():
        a = raw_input("updating %s, confirm? (y/n)"%p)
        if a =='y':
            try:
                install(['-U']+[p])
            except:
                print "Update of %s failed!"%p
        else:
            print "Skipping %s"%p
        print "Done!"
            
print "You have %s packages currently managed through Easy_install"%len(plist)
print plist
print ("Downloaded from http://www.snipplr.com/view.php?codeview&id=56085")
print ("Credits to unknown author")
ans = raw_input('Do you want to update them... (N)ot at all, (O)ne-by-one, (A)utomatically (without prompting)')
if ans == 'N':
    sys.exit()
elif ans == 'O':
    stepUp()
elif ans == 'A':
    autoUp()
else:
    pass 