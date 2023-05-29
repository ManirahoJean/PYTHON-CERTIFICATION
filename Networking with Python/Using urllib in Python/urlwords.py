# Using urllib in python
"""
Since HTTP is so common, we have a library that does all the
socket work for us and makes web pages look like a file
"""

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# Code: http://www.py4e.com/code3/urllib1.py

print("\n")

# Like a file

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

print("\n")

# Reading Web Pages

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

# Question
# What will the output of the following code be like?
"""
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
-Just contents of "romeo.txt".
-A header and the contents of "romeo.txt".
-A header, a footer, and the contents of "romeo.txt".

"""
