# String Parsing Examples

data = "From Stephen.marquard@uct.ac.za sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1: sppos]
print(host)
"""
Extracting a host name using find and string 
slicing
"""

print("\n")

# Double split Pattern

"""
sometimes, we split a line one way, and then grab one of the pieces
of the line and split that piece again 
"""
line = "From Stephen.marquard@uct.ac.za sat Jan 5 09:14:16 2008"
words = line.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])

print("\n")

# The Regex Version

import re
lin = "From Stephen.marquard@uct.ac.za sat Jan 5 09:14:16 2008"
y = re.findall('@([^ ]*)', lin)
print(y)

"""
'@([^ ]*)': Look through the string untill you find an at sign 
[^ ]: Match non-blank character
*: Match many of them 
"""
y = re.findall('^From .*@([^ ]*)', lin)
print(y)

"""
'^From .*@([^ ]*)': 
^From: Starting at the beginning of the line,look for the string "From"
"""

# Spam confidence

"""
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
    print('Maximum: ', max(numlist))

print("\n")
"""

# Escape Character
"""
If you want a special regular expression to just behave normally
(most of the time) you prefix it with "\"
"""
x = "We just received $10.00 for cookies. "
y = re.findall('\$[0-9. ]+', x)
print(y)
