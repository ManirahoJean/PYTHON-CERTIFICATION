# Find the smallest value
smallest_so_far = -1
print("Before", smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("After", smallest_so_far)

print("\n")

"""
Here, no number which is less than -1, so the code will not work as expected, 
we don't know the value to start with, so how do we fix this?
"""

smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

"""
we still have a variable that is the smallest so far.
the first time the smallest is NOne, so we take the first value to be 
the smallest
"""

"""
-The <<is>> and <<is not >> operators
-python has <<is>> operator that can be used for logical expressions
-implies ""is the same as""
-similar to, but stronger than ==
-<<is not>> is also a logical operator
-0 == 0.0 True
-0 is 0.0 False
-<<is>> is used for boolean

"""