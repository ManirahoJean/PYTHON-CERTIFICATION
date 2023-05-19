# The get method in the dictionaries
"""
The pattern of checking if the key is already in the dictionary and assuming
a default value if the key is not there is so common that there is a method called get()
that does this for this
The default value if the key doesn't exist(and no Traceback)
"""

counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
for name in names:
    if name in counts:
        x = counts[name]
    else:
        x = 0

    x = counts.get(name, 0)
print(counts)

# Simplified counting

"""
We can use get() and provide a default value of zero when the key is not 
yet in the dictionary- and just add one 
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# What will the following code print?

counts = {'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))