# Search using boolean Variable
found = False
print("Before", found)

for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

"""
If we just want to search and now if a value was found, we use variable that starts with False
and is set to True as soon as we found what we're looking for.  
"""