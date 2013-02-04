#!/usr/bin/python
#counts occurrence of the strings in *.txt file - extension required

fname=raw_input("Enter filename with extension where data resides: ")
nos=int(input("Enter numbers of strings to be counted: "))
f=open(fname, 'r')
str=f.read()
for broj in range (1, nos+1):
	print ("String %r") %broj
	string=raw_input("Enter string: ")
	cnt=str.count(string)
	print ("%r : %r") %(string, cnt)
print ("Done!")
fn.close()
