# Function Class [Either the function will Peroform a task or Return a value]
def greet(first_name, last_name):
    # print(f"Hi {first_name} {last_name}")
    return f"Hi {first_name} {last_name}"


msg_for_me = greet("John", "Doe")
print(msg_for_me)

# In Python all function return "None" by default unless specifically told to return a value. "None" is an object that represents the absence of a value.


def full_name(name):
    print(f"{name}")


print(full_name("mosh hamedani"))

# xargs class


def multiplying(*values):
    total = 1
    for number in values:
        total *= number
    return total


print("start")
print(multiplying(1, 2, 3, 4, 5))


# xxargs class
def save_user(**user):
    print(user)
    print(user["age"])


save_user(id=1, name="Jp Morgan", age=98)

# For Debugging
# Mark/Unmark the line from where you want to debug = F9
# Start the debugger = F5
# Move forward = F10
# If its a Function call = F11
# Stop the debugger = Shift+F5


# Exercise
def fizz_buzz(value):
    if (value % 3 == 0) and (value % 5 == 0):
        return "fizz & buzz"
    if value % 3 == 0:
        return "fizz"
    if value % 5 == 0:
        return "buzz"
    return value


print(fizz_buzz(700))
