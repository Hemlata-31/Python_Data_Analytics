# Converting data types in Python is called typecasting. It is used to convert one data type into another data type.
# For example, we can convert an integer to a string, a string to a float, and so on. Python provides several built-in functions for typecasting.
# Type conversion performs automatically while we have to manually perform typecasting.

# Type conversion (not perform string and integer addition)
a = 2
b = 4.75 

sum = a + b
print("Sum:", sum) #float is superior to int. So it becomes 2.0 + 4.75

# Typecasting (perform string and integer addition)
x = 5
y = "10"
sum = x + int(y) # we have to convert string into integer using int() function
print("Sum:", sum)

# Other functions for typecasting are float(), str(), bool(), list(), tuple(), set(), dict() etc.