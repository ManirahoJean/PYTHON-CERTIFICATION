# counting in loop

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("After", zork)

print("\n")

# Summing in loop

other_zork = 0
for other_thing in [9, 41, 12, 3, 74, 15]:
    other_zork = other_zork + other_thing
    print(other_zork, other_thing)
print("After", other_zork)

"""
To add a value we encounter in loop, we introduce a sum variable that
starts at 0 and we add the value to the sum each time through the loop  
"""

