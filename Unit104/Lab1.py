# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
'''
My name is [Your Name]
Favorite food: [Your Favorite Food]
Dream job: [Your Dream Job]
'''

# Assign 5 different data types to 5 different variables. At least one datatype must be a string.
var_int = 42
var_float = 3.14
var_str = "Hello, World!"
var_bool = True
var_list = [1, "two", 3.0, False, "five"]

# Print the length of your string.
print(len(var_str))

# Create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"
savvy = "Learning Python is Awesome!"

# Replace "Awesome" with "great" in the string.
savvy = savvy.replace("Awesome", "great")

# Create and assign 3 more variables called name, age, and length using the multi-variable naming method.
name, age, length = "John", 25, 180

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase...
# "Hi my name is (name), I am (tall) and (so) old today."
miniBio = f"Hi, my name is {name}, I am {length} cm tall and {age} years old today."

# Create a list of at least 5 elements of mixed data types.
my_list = [1, "apple", 3.14, True, "five"]

# Replace a part of it with something else.
my_list[1] = "banana"

# Append or insert several more items to the list.
my_list.append(False)
my_list.insert(2, "orange")
my_list.extend(["grape", 7.8])

# Find and print the length of the list.
print(len(my_list))

# Slice a sub-section of the 1st list and save it to a different 2nd list.
second_list = my_list[1:4]

# Print the 2nd list.
print(second_list)

# Extend your original list with the 2nd list sliced above.
my_list.extend(second_list)

# Create a new list called "simList" containing at least 5 elements of the same data type,
# either string, integer, float, or Boolean.
simList = [42, 7, 3, 1, 99]

# Sort "simList" and print the list.
simList.sort()
print(simList)

# Copy the "simList" list to another 3rd list.
third_list = simList.copy()

# Add the 2nd and 3rd lists together into a 4th list.
fourth_list = second_list + third_list




