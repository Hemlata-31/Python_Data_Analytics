# Set is the collection of unordered items.
# Each element in the set must be unique & immutable.
# repeated elements stored only once
# sets is mutable but its elements are immutable

sets = {1, 2, 3, 4, 5, 2, 1, "Hello", "World"}
print(sets)
print("Total number of items:-", len(sets)) #duplicate values does not count

# Empty set 
emp_set = set()

# Methods
print("Adding elements:-" , sets.add("morning"))
print(sets)
print("Remove element:-" , sets.remove(5))
print(sets)
print("Remove an random value:-" , sets.pop())
print("To empty the set:-" , sets.clear())
print(sets)

print("\n")
set1 ={3, 5, 7, 1, 8, "Morning", "Hello"}
set2 = {1, 2, 6, 8, 4, "Good"}
print("Union:-" ,set1.union(set2)) # merge set1 and set 2 value
print("Intersection:-", set1.intersection(set2)) # combine common values of set1 and set2
