# Strings is data type that stores a sequence of characters
# String creation
str1 = "This is my first string" # mostly used
str2 = 'This is my second string'
str3 = '''This is my third string'''

# String Operations 

str1 = "Hello"
print(len(str1)) # Length of string
str2 = "Hemlata"
print(len(str2)) # Length of string and spaces are also counted in length of string

final_str = str1 + " " + str2

print(final_str) # Concatenation
print(str1 * 3) # Repetition

# Indexing starts from 0 and it is used to access elements at particular places
print(str1[0]) # Accessing first character
print(str2[3]) # Accessing fourth character

# Slicing is used to access a range of characters from string, str[starting_idx:ending_idx] and starting include while ending exclude in output
print("Accessing first three characters of str1:", str1[0:3]) 
print("Accessing characters from second to fourth of str2:", str2[1:4])
print("Accessing first three characters of str1:", str1[:3])
print("Accessing characters from second to last of str2:", str2[1:]) 
print("Accessing last three characters of str1:", str1[-3:]) 

# String Functions or methods 
str = " I am learning python programming language"
print("Checking if str ends with 'lo':", str.endswith("lo"))
print("Checking if str starts with 'I':", str.startswith("I"))
print("Capitalizing str:", str.capitalize())
print("Converting str to upper case:", str.upper())
print("Converting str to lower case:", str.lower())
print("replacing 'Hem' with 'Hemu' in str2:", str2.replace("Hem", "Hemu"))
print("Finding index of 'l' in str2:", str2.find("l"))
print("Counting number of 'a' in str2:", str2.count("a"))

