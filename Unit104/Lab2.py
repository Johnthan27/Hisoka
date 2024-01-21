# Variables for demonstration
a = 5
b = 10

# Equals: a == b
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Not Equals: a != b
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Less than: a < b
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Less than or equal to: a <= b
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is greater than b")

# Greater than: a > b
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is not greater than b")

# Greater than or equal to: a >= b
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# Using 'and' between conditions
if a > 0 and b > 0:
    print("Both a and b are positive")

# Using 'or' between conditions
if a < 0 or b < 0:
    print("At least one of them is negative")

# Nested if statement
if a > 0:
    if b > 0:
        print("Both a and b are positive")
    else:
        print("a is positive, but b is not")

# if statement with 'pass' to avoid errors
if a < 0:
    pass
else:
    print("a is not negative")
