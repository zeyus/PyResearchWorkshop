"""01_simple.py

This shows some basic python concepts.

"""

# This is a comment.  It is not executed by the interpreter.

# This is a string.  It is a sequence of characters. You can use single or double quotes.
"Hello World"

# Strings (and almost anything else) can be assigned to a variable
# variables can be named however you like, but they must start with a letter or underscore
# and they should be the same as a reserved word (like print). You also can't use spaces.
my_string = "Hello World"
another_string = "Goodbye World"

# Naming of variables is important, they should be descriptive of what they contain
# and they should be consistent.  This is called "naming conventions"
# For example the above variables could be named:
greeting = "Hello World"
farewell = "Goodbye World"

# if you want a message displayed on the screen, you can use the print function
print(greeting)
print(farewell)

# You can insert variable into strings in may different ways, the easiest is to
# create a "formatted string" using the f-string syntax
print(f"Greeting: {greeting}, Farewell: {farewell}")

# New lines are created with the \n character
print(f"Greeting: {greeting}\nFarewell: {farewell}")

# Basic math uses the same symbols as you would expect

# Addition
print(f"1 + 1 = {1 + 1}")
# Subtraction
print(f"3 - 2 = {3 - 2}")
# Multiplication
print(f"2 * 3 = {2 * 3}")
# Division
print(f"5 / 4 = {5 / 4}")
# Modulus (remainder)
print(f"5 % 4 = {5 % 4}")
# Exponentiation
print(f"2 ** 3 = {2 ** 3}")

# You can also use variables in math
a = 1
b = 2
c = 3
print(f"a + b + c = {a + b + c}")

# or assign the result of math to a variable
d = a + b + c
print(f"d = {d}")

# Reusing Code: Funcitons
# Functions are a way to reuse code.  They are defined using the def keyword
# followed by the function name and a set of parenthesis.  The parenthesis
# can contain arguments (or parameters) that are passed to the function.
# The function definition ends with a colon (:)

# here is a function that prints "Hello World", and does not take any arguments
def my_function():
    print("Hello World")

# to call a function, you use the function name followed by parenthesis
my_function()

# here is a function that takes two arguments and prints them
def my_other_function(arg1, arg2):
    print(arg1)
    print(arg2)

# to call a function with arguments, you pass the arguments in the parenthesis
my_other_function("Hello", "World")
my_other_function(greeting, farewell)

# Functions can also return values.  This is done with the return keyword
# here is a function that returns the sum of two numbers
def sum(a, b):
    return a + b

# to use the return value of a function, you assign it to a variable
result = sum(1, 2)
print(f"result = {result}")

# or use it directly in another function call   
print(f"sum(1, 2) = {sum(1, 2)}")

# Functions can also have default values for arguments
def my_function_with_defaults(arg1="Hello", arg2="World"):
    print(arg1)
    print(arg2)

# if you call a function with default arguments, you don't need to pass them
my_function_with_defaults()
my_function_with_defaults("Goodbye")
my_function_with_defaults(arg2="Goodbye")

# Note that any variables created within a function are not available outside of the function
# This is called "scope"
# e.g. You cannot access arg1 or arg2 outside of my_function_with_defaults

# Conditions, Loops, and Lists

# Conditions are used to control the flow of a program.  They are defined using
# the if keyword followed by a condition.  The condition is a boolean expression
# that evaluates to True or False.  The condition ends with a colon (:)
# The code that is executed if the condition is True is indented.
# The indentation can be any number of spaces, but it must be consistent.
# The code that is indented is called a "block" of code.
# The block of code ends when the indentation ends.

# here is a function that prints "Hello World" if the argument is True
def my_function_with_condition(show=True):
    if show:
        print("Hello World")

# to call a function with a condition, you pass the condition in the parenthesis
my_function_with_condition(True)
my_function_with_condition(False)

# Conditions can also be combined with the and, or, and not keywords
# "and" is True if both conditions are True
# "or" is True if either condition is True
# "not" is True if the condition is False
# Conditions can also be grouped with parenthesis
# e.g. (a and b) or (c and d)
# examples:
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")
print(f"not False = {not False}")
print(f"True and (True or False) = {True and (True or False)}")

# Conditions can also be combined with the elif and else keywords, which are
# used to define what happens if the condition is False
# elif is short for "else if"

# here is a function that prints "Hello World" if the argument is True
# and prints "Goodbye World" if the argument is False
def my_function_with_condition_else(greeting=True):
    if not isinstance(greeting, bool): # Check if greeting is a boolean (True or False)
        print("Argument must be True or False")
    elif greeting: # This is the same as elif greeting == True
        print("Hello World")
    else: # This is the same as elif greeting == False, as there are no other options
        print("Goodbye World")

# now you can call the function with different arguments
my_function_with_condition_else(True)
my_function_with_condition_else(False)

# You can see in the my_function_with_condition_else function a function
# that we did not define, isinstance.  This is a built-in function that
# checks if a variable is of a certain type.  In this case, we are checking
# if the argument is a boolean.  The isinstance function takes two arguments,
# the variable and the type.  It returns True if the variable is of the type
# Common types in python are:
# int - integer (whole number, e.g. 1, 2, 3)
# float - floating point number (decimal, e.g. 1.5)
# str - string (sequence of characters)
# bool - boolean (True or False)
# list - list (see below)
# tuple - tuple (like a list, but immutable, meaning it cannot be changed)
# dict - dictionary (like a list, but with key/value pairs)

# A list in python is a sequence of items.  The items can be any type.
# Lists are defined using the square brackets [] and the items are separated
# by commas.  Lists can be assigned to variables.
# e.g.
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Lists can be accessed by index.  The index starts at 0.
# e.g.
print(f"my_list[0] = {my_list[0]}")
print(f"my_list[1] = {my_list[1]}")

# Lists can also be sliced.  This is done by specifying a start and end index
# separated by a colon (:)
# e.g.
print(f"my_list[0:2] = {my_list[0:2]}")
print(f"my_list[1:3] = {my_list[1:3]}")

# Loops are used to repeat code.  They are defined using the for keyword
# followed by a variable name, the in keyword, and a list.  The code that
# is executed in the loop is indented.

# here is a function that prints each item in a list
def my_function_with_loop(my_list):
    for item in my_list:
        print(item)

# now you can call the function with different arguments
my_function_with_loop(["hi", "bye"])
my_function_with_loop(my_list)

# Loops can also be combined with conditions
# here is a function that prints each item in a list if the item is greater than 2
def my_function_with_loop_and_condition(my_list):
    for item in my_list:
        if item > 2:
            print(item)

# now you can call the function with different arguments
my_function_with_loop_and_condition(my_list)

# Finally, let's look at dictionaries.  Dictionaries are like lists, but instead
# of accessing items by index, you access them by key.  The key can be any type.
# Dictionaries are defined using curly braces {} and the items are separated
# by commas.  Items are defined as key/value pairs separated by a colon (:).
# Dictionaries can be assigned to variables.
# e.g.
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)

# Dictionaries can be accessed by key.
# e.g.
print(f"my_dict['a'] = {my_dict['a']}")
print(f"my_dict['b'] = {my_dict['b']}")

# Dictionaries can also be looped over.  This will loop over the keys.
# e.g.
for key in my_dict:
    print(key)

# Dictionaries can also be looped over with the items() function.  This will loop over the key/value pairs.
# e.g.
for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")

# Dictionaries can also be looped over with the values() function.  This will loop over the values.
# e.g.
for value in my_dict.values():
    print(value)


# There's a lot more to it but that's the basics. Check the resources file for more info.
# https://github.com/zeyus/PyResearchWorkshop/blob/main/resources.md