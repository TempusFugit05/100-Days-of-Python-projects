# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
#______________________________________________________________

# Singe parameter function
def greet(name): # "name" is the parameter
    print("test")
    print("1")
    print(name)
#greet(input("What is your name? ")) #This input is the argument

#______________________________________________________________

# Func with double the parameters. Thus, the name
def double_trouble(name, weather):
    print(f"Hello {name}, today is {weather}")
#double_trouble(input("What's your name?"), input("What is the weather?"))

#______________________________________________________________

# It is also possible to manually assign the arguments by equating the arguments in the func
double_trouble(weather="nice", name="Adam")

#______________________________________________________________

