# Search and Replace

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

line = 'Please have a good day!'
print(line.startswith('Please'))
print(line.startswith('p'))

data = 'From stephen.marquard@uct.ac.za Sat June 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1: sppos]
print(host)

# challenge
word = "bananana"
i = word.find("na")
print(i)