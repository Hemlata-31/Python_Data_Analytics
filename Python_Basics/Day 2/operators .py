# Operators are symbols used to perform operations on variables and values or between two values or operands. 
# Python divides the operators in the following groups:

# Arithmetic operators (+, -, *, /, %, **, //)
a = 3
b = 6
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)  # we always get floating number
print("Remainder:", a % b)
print("Power:", a ** b)
print("Floor Division:", a // b)
print("\n")

# Comparison / Relational operators (==, !=, >, <, >=, <=)
c = 60
d = 50
print("Equal:", c == d)
print("Not Equal:", c != d)
print("Greater Than:", c > d)
print("Less Than:", c < d)
print("Greater Than or Equal:", c >= d)
print("Less Than or Equal:", c <= d)
print("\n")

# Assignment operators (=, +=, -=, *=, /=, %=, **=, //=)
e = 10
f = 35
print("Initial Value of e:", e)
print("Initial Value of f:", f)
e += f  # e = e + f
print("After e += f, Value of e:", e)
e -= f  # e = e - f
print("After e -= f, Value of e:", e)
e *= f  # e = e * f
print("After e *= f, Value of e:", e)
e /= f  # e = e / f
print("After e /= f, Value of e:", e)
print("\n")

# Logical operators (and, or, not)
g = True
h = False
print("g and h:", g and h)
print("g or h:", g or h)
print("not g:", not g)
