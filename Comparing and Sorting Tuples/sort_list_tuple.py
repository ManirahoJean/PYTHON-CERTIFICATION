# Comparing and Sorting Tuples
d = {'a': 10, 'b': 1, 'c': 22}
d.items()

dict_items = ([{'a': 10, 'c': 22, 'b': 1}])
sorted(d.items())


# Sort by Values not by keys

for k, v in d.items():
    print(k, v)

temp = list()
for k, v in d.items():
    temp.append((v, k))
print(temp)

print("\n")

# Reverse order

temp = sorted(temp, reverse=True)
print(temp)

print("\n")

# Top 10 common words

fhand = 'From stephen.marquard@uct.ac.za Sat June 5 09:14:16 2008'
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


lst = list()
for key, val in counts.items():
    newtupe = (val, key)
    lst.append(newtupe)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(val, key)

print("\n")

# Even shorter version

c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k)for v, k in c.items()]))
