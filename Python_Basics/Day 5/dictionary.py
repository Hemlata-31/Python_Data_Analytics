# Dictionaries are used to store data in key : value pairs 
# They are unordered, mutable, & don't allow duplicate keys

dict = {
    "name" : "Hemu",
    "age"  : 20,
    "cgpa" : 8.0,
    "marks" : [80, 79, 85],
    "subjects" : ("Java" , "DSA", "OOP"),
}
print(dict)
print(type(dict))

print("Print an value of key name :-" , dict["name"])
dict["surname"] = "Kumawat"
print("Adding an key value pair:-", dict["surname"])

dict["name"] = "Hemlata"
print("use overwrite for changing an name of an key{name}:-" , dict["name"])

# create an null dict
null_dic = {}

# Nested dictionaries 
print("\n")
student = {
    "name" : "AAyu",
    "class" : 9,
    "subjects" :{
        "maths" : 75,
        "phy" : 80,
        "chem" : 85,
    }
}
print(student)
print("Maths marks:-" ,student["subjects"]["maths"])

# Methods in dictionary
print("\n")
print("To return all keys in list form:- ",list(dict.keys())) 
print(len(list(dict.keys())))
print("To return all values:- ", dict.values())
print("To return all (key, value) pairs as tuples:- ", dict.items())
print("To return the key according to value:-",dict.get("name")) #if empty or key name is not in dictionary then it return null but normal one give error
new_dict= {"city" : "Indore"}
print("To insert the specified items{} to the dictionary:-",dict.update(new_dict))