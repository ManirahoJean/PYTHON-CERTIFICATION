# Looping through strings
# Using while statement

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print("\n")
# Using for loop statement

fruit = 'banana'
for letter in fruit:
    print(letter)

# Looping and counting

"""
This is a simple loop that loops through each letter in a string 
and counts the numbers of times the loop encounters in the 'a' character
"""

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

