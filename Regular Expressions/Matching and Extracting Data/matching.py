"""
-re.search returns a True/False depending on whether the string matches
the regular expression
-if we actually want the matching string to  be extracted, we use re.findall()
"""
# Greedy matching

import re
x = "my 2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+', x)
print(y)
# [0-9] is considered as one character, one digit or more digits

print("\n")

y = re.findall('[AEIOU]+', x)
print(y)
# Here the output is empty list [], because of the capital letters

"""
The repeat characters (* and +) push outward in both directions (greedy)
to match the largest possible string 
"""

x = "From: Using the : Character"
y = re.findall('^F.+:', x)
print(y)

"""
^F: First character in the match is F
: last character in the match is :
+: one or more characters
"""
print("\n")

# NonGreedy Matching
"""
Not all regular expression repeat codes are greedy!
If you add a ? character, the + and * chill out a bit...
"""
x = "From: Using the : Character"
y = re.findall('^F.+?:', x)
print(y)

print("\n")

# Fine-Tuning String Extraction

"""
You can refine the match for the re.findall() and separately determine 
which portion of the match is to be extracted by using parentheses
"""

x = "From Stephen.marquard@uct.ac.za sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+', x)
print(y)

"""
\S+@\S+: at least non-white space character 
"""
y = re.findall('^From (\S+@\S+)', x)
print(y)

print("\n")

# Question
# What will the following program print?:

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
