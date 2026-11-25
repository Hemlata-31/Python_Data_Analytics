# Control Statements are used to control the flow of execution in a program. 
# They allow you to make decisions, repeat actions, and handle different scenarios based on conditions.
# Types of Control Statements in Python:
# 1. Conditional Statements (if, elif, else)    

age = int(input("Enter your age: "))
if(age >= 18):
    print("You are eligible to vote.")
elif(age <18):
    print("You are not eligible to vote.")
else:
    print("Invalid age entered.")

# Nesting :- means placing one control statement inside another control statement. 
if(age >= 18):  
    print("You are eligible to vote.")
    if(age >= 21):
        print("You are also eligible to drive.")
    else:
        print("You are not eligible to drive.")