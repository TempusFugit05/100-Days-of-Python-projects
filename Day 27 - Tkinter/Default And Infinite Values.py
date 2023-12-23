# It's possible to give a function a default value to be used as an argument
def my_func(a=5):
    return a**2


# Here the function will use the default value which is 5
print(my_func())

# Here the function will use the provided value
print(my_func(a=12))


# It is also possible to create functions that would take any number of arguments
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add_all(1,2,3,4,5,6,7,8,9,10))


# It's even possible to create a function that takes an unlimited amount of positional arguments
# It works by creating a dictionary that stores the key as argument name and value as the value of the argument
# It is however, impossible to run this code if a key value wasn't specified (for example if we wouldn't specify
# the add argument)
def unlimited_function(**argument):
    total = 0
    total += argument["add"]
    total = total*argument["multiply"]
    total -= argument["subtract"]
    return total


print(unlimited_function(add=3, multiply=42, subtract=12))


# To mitigate this in a context like class creation, we could use the get function
class Weapon:
    def __init__(self, **optional_arguments):
        self.damage = optional_arguments.get("damage")
        self.range = optional_arguments.get("range")


# Here, the rock will be assigned a damage of 1 but since the range of this rudimentary weapon is not relevant
# we could not specify the range and in this case the value of this attribute would be None.
rock = Weapon(damage=1)
print(rock.damage, rock.range)