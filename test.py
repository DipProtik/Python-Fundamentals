# START 15-03-2025

import math
print("hello world !")
print("*" * 10)

# To open user settings (ctrl+shift+P)
# (ctrl+alt+n) to run the code(save before run)

x = 1
print(x)

# Variable Class
# [primitive types in python =number, boolean, string]
# Python is a Case Sensitive Language. "TRUE"/"true" will not be accepted as boolean value. The decalration should be like [course_name ="True"]

students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"

# String Class
fruit = "Jackfruit"
print(len(course_name))
print(course_name[0:5])  # Slice a string
# if we don't use start and end index it will return the original string
print(course_name[:], "\n", fruit[1:-1])


# Escape Sequence
course1_name = "Data \'Structure"
course2_name = "Data \"Structure"
course3_name = "Data \\Structure"
course4_name = "Data \nStructure"
print(course1_name, course2_name, course3_name, course4_name)

# Formatted Strings
first = "John"
last = "Doe"
full_name = f"{first} {last}"
print(full_name)

# When using formatted strings we can put any valid expressions in between curly braces
full_name2 = f"{len(first)} {20+25}"
print(full_name2)

# String Methods
# Everything in python is an OBJECT. An object has functions that we call methods and we can access them with a dot notation.
course5_name = " C Programming "
# As Python is case sensitive it will return -1 for the FIND() used at last of the following print statement, that means it was not found in the original string
print(course5_name.upper(), "\n", course5_name.lstrip(), "\n",
      course5_name.find("mmi"), "\n", course5_name.find("Mmi"))

# it will return a boolean value
print("Pro" in course5_name, "C" not in course5_name)

# Numbers
print(10 / 3, "\n", 10 // 3, "\n", 10 % 3, "\n", 10 ** 3)
print(round(2.99), abs(-3.99))  # abs() is used to get the absolute value

# To work with complex math problem we can import the MATH MODULE. A module is like a separate file with some python code. Now, MATH in this program is an object. So we can use dot notation to access all the functions available in this object.
print(math.ceil(22.56))

# Type conversion[int(x), float(x), bool(x), str(x)]

# x = input("x: ")  # user input is always a STRING value
# y = int(x)+1
# print(f"x: {x}, y:{y}")

# When we GET [ "" =empty string, 0 =number zero, None =absence of a value ] they will return false in BOOLEAN CONTEXT. Otherwise every value/string is TRUE.

# CONTROL STATEMENT(When you use a IF statement you should always end your statement with a colon(:))

temperature = 15
if temperature > 30:
    print("it's warm")
elif temperature > 20:
    print("it's nice and cozy")
else:
    print("it's cold")
print("done")

# Ternary Operator
age = 12
message = "Eligible" if age >= 18 else "not eligible"
print(message)

# Logical operator(In python logical operators are SHORT-CIRCUIT)
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible for the role")
else:
    print("Not eligible")

age_ = 22
# In python we can write the conditional operation in this way. It is known as CHAINING COMPARISION OPERATORS
if 18 <= age < 65:
    print("teenage")
else:
    print("Old")


# Loops
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# For_ELSE
price = 500
for latest_price in range(100, 1000, 101):
    print(f"latest_price:{latest_price}")
    if price == latest_price:
        print("Value Matched")
        break
else:
    print("value didn't matched")


# RANGE is an object of type range. It is one of the complex data type in Python. This range object is ITERABLE
for x in range(5):
    print(x)

# LIST is another complex data type.
for x in [3, 33, 333, 3333, 33333]:
    print(x)

# STRING is also iterable.
for y in "Java":
    print(y)

# While Loop
command_str = ""
while command_str != "quit":
    command_str = input("Enter the string:").lower()
    print("Echo", command_str)

# To avoid infinite loop it is always preferable to use the BREAK statement
while True:
    command = input(">>>===>>>")
    print("Echo: ", command)
    if command.lower() == "oui":
        break
