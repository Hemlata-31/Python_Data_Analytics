print("PROGRAM 1 TO PRINT NUMBERS FROM 1 TO 10")

n = 1
while n <= 10:
    print(n)
    n += 1

print("END", "\n")

print("PROGRAM 2 TO PRINT NUMBERS FROM 10 TO 1")

n = 10
while n >= 1:
    print(n)
    n -= 1

print("END", "\n")

print("PROGRAM 3 TO PRINT MULTIPLICATION TABLE OF NUMBER N")

n = 4
i = 1
while i <= 10:
    print(n*i)
    i += 1

print("PROGRAM 4 TO PRINT FOLLOWING LIST [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] USING A LOOP")

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
colors = ["BLACK", "WHITE", "BLUE", "RED"]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

print("PROGRAM 5 TO SEARCH FOR A NUMBER X IN THIS TUPLE")

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 81
i = 0

while i < len(nums):
    if nums[i] == x:
        print("Found at index:-", i)
        break
    else:
        print("finding...")
    i += 1
print("END")

print("\n WRITE A PROGRAM TO FIND THE SUM OF FIRST N NUMBERS")

n = 10
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
     
print(sum)