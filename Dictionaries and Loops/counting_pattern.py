# Counting pattern
"""
the clown ran after the car and the car run into the tent
and the tent fell down on the clown and the car
"""

counts = dict()
print("Enter a line of text: ")
line = input('')
words = line.split()
print("Words: ", words)
print("counting...")

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts', counts)

"""
The general pattern t0 count the words in a line of text is to 
split the line into words and use a dictionary to track the count of
each word independently
"""

# Question
# What will the following code print?

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
