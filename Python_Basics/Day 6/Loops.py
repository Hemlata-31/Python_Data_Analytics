# Loops are used to repeat instructions.
# Types of loops:- while and for 


# 1. while loop:- while condition : some work
 
count = 1
while count <= 5 :
    print("Hello!!", count)
    count += 1

print("\n")

# Break and Continue
# Break :- used to terminate the loop when encountered
# Continue :- terminate execution in the current iteration & continues execution of the loop with the next iteration 

i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("End")
print("\n Continue Keyword")

i = 1
while i <= 5:
    if(i%2 == 0):
     i += 1
     continue # even numbers will skip and other print
    print(i)
    i += 1
print("END")
     
# For Loops are genrally used for sequential traversal.
# for traversing list, string, tuples etc.

print("\nFOR LOOP")

list = [1, 2, 3, "Lily", "Tulip"]

for num in list :
   print(num)


print("\n FOR ELSE LOOP")

tuple = (1, 2, 3, 4, 5)

for nums in tuple:
   if(nums == 4):
      print("FOUND")
      break
   print(nums)
else:
   print("END")

# range() :- function returns a sequence of numbers,
# starting from 0 by default , and increments by 1(by default)
# ans stops before a specified number
# range(start?, stop, step?) in this start and step is optional and step means --> increase 

for i in range(5):
   print(i)

print("\n odd numbers")
for j in range(1, 20, 2):
   print(j)

# Pass statement is a null statement that do nothinh used as a placeholder

for a in range(10):
   pass

print("Null statement")