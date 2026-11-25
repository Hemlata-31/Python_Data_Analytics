# Taking an input from the user 
# we use input() function to take input from the user.

input1 = input("Enter your name: ")
input2 = input("Enter your age: ")
print("Hello!!", input1, "your age is", input2)
print(type(input1), type(input2)) # <class 'str'> <class 'str'>  (input() function always takes input as string)

# To take input as integer we have to convert string into integer using int() function.
input3 = int(input("Enter your marks: "))
print("Your marks are:", input3)
print(type(input3))
