# It is possible to create, read and write to a file using python in order to preserve information between
# program runs

# Defining file name
file_name = "test_file"

# Opening file and storing contents as a variable
file = open(file_name)

# Using the read function in order to save the contents of the file to a variable
contents = file.read()

# Printing the contents of the file
print(contents)

# Closing the file to free up resources
file.close()

# An alternative way to open files is like so:
with open(file_name) as file:
    contents = file.read()
    print(contents)
    # This method will close the file automatically

"""# This code will give an error since we're trying to write to a file that is set to read-only
with open(file_name) as file:
    file.write("Trololo")"""

# To change that, we have to specify that this file can be writen to using 'w' as a parameter
# *** This will completely rewrite the file contents ***
# If the file does not yet exist, the program will automatically create one with the same name
with open(file_name, "w") as file:
    file.write("Trololo")

with open(file_name) as file:
    contents = file.read()
    print(contents)

# This will append (add) our text to the file instead of rewriting it completely
with open(file_name, "a") as file:
    file.write("\nTest test 123")

# It's also possible to open the file using the absolute file location
with open("C:/Users/Adam/PycharmProjects/pythonProject/Day 24 - Reading And Writing To Files/test_file") as file:
    contents = file.read()
    print(contents)