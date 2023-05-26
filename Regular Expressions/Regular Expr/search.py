"""
A RegEx, or Regular Expression, is a sequence of characters that
forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
Python has a built-in package called re, which can be used to work with Regular Expressions.

"""
# Search the string to see if it starts with "The" and ends with "Spain":

import re
txt = "There is rain in Rwanda"
msg = re.search("^The.*Rwanda$", txt)
print(msg)
print("\n")

fhand = 'From stephen.marquard@uct.ac.za Sat June 5 09:14:16 2008'

for line in fhand:
    line = line.rstrip()
    if line.find('From ') >= 0:
        print(line)

for line in fhand:
    line = line.rstrip()
    if re.search("^From", line):
        print(line)

message = re.search("From", fhand)
print(message)
print("\n")

# Using re.search like startswith

for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)
for line in fhand:
    line = line.rstrip()
    if re.search('^from', line):
        print(line)


txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
