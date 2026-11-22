# 30 Days challenge  (comment:- When we have to add some information in code using ctrl + /)
# Multiline comments using (''')
'''
Starting my journey as an data analyst
Python is such an good language to learn for data analyst

'''
# Escape Sequence Character (when we have to insert character that cannot be directly used in string)
# backslash is used with character 
#print("This will \"execute\"") When we have to print text withdouble quotes
print("Hello!! \nHemlata Kumawat, in 1-Day of \"Python Data Analytics Course\"")   

#print Statement 
#print("hey!!", 31, 5, sep = "~")

# Variables are used to store data in memory
# Variable name should not start with number and special character
a = 1 #integer
b = True #boolean
c = "Hemu" #String
d = None #NoneType
print(a, b, c, d, "\n")

# Data type specifies which type of value a variable can hold
# Numeric data:- int, float, complex
# Text data: str
# Boolean data: True or False
# Sequenced data: list, tuple, range
# Mapped Data: dict
print("\nData Types")
print("Type of a:", type(a)) # <class 'int'>
print("Type of b:", type(b)) # <class 'bool'>
print("Type of c:", type(c)) # <class 'str'>
print("Type of d:", type(d)) # <class 'NoneType'>
print("\n")

#List:- A list is a collection which is ordered and changeable. Allows duplicate members.Separated by comma and enclosed in square brackets.
list1 = [1, 2, 4.5, [-4, 5], ["apple", "banana"]] 
print("list1:",list1)
print("\n")

#Tuple:- A tuple is a collection which is ordered and unchangeable. Allows duplicate members.Separated by comma and enclosed in parentheses.
tuple1 = (("Rose", "Lily"), (1, 2, 3), (4.5, 5.6))
print("tuple1:",tuple1)
print("\n")

# Dictionary:- dictionary is a collection which is unordered, changeable and indexed. No duplicate members. Separated by comma and enclosed in curly brackets.
dict1 = {"name": "Hemu",
          "\nage": 20, 
          "\ncity": "Delhi"}
print("dict1:",dict1)
