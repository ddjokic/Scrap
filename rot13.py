#!/usr/bin/env python

# shamelessly copied from http://www.leancrew.com/all-this/

from string import maketrans
from sys import stdin, stdout


alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
rot13 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM9876543210'
r13table = maketrans(alpha, rot13)

orig = raw_input("Get String: ")
print (orig.translate(r13table))