#!/usr/bin/python3
a = 89
b = 10
temp = a
a = b
b = temp
a, b = b, a
print("a={:d} - b={:d}".format(a, b))