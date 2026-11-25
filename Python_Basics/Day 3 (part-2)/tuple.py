# Tuples are just like list but they are immutable.
# Tuples are created using an brackets ().


tuple = (1,) # it is identified as tuple
print(type(tuple))
tup = (1) # it is identifies as an int 
print(type(tup))

# Tuple methods
tup = (1, 2, 3, 4, 3, 6)
print("Index of first occurance of an element in tuple at index 2:-", tup.index(2))

print("Count total occurences of an element 3 in tuple:-", tup.count(3))

