# List comprehension can significantly cut down on the amount of time it takes to change values in a list on mass
# Here's an example on how this might help

#----------------------------------------------------------------------------------------------------------
# Here we want to increase by one each of its items
num_list = [1, 2, 3, 4, 5]
modified_list = []
for n in num_list:
    modified_list.append(n+1)

# print(modified_list)
#----------------------------------------------------------------------------------------------------------
# Instead we could do the same thing using list comprehension
num_list = [1, 2, 3, 4, 5]

# Here we have a for loop that iterates over every item inside the list and replaces the current item with
# itself + 1
num_list = [n+1 for n in num_list]

# We've cut down substantially the amount of code we have to write to achieve this goal
# print(num_list)
#----------------------------------------------------------------------------------------------------------
# We can use this for strings as well
name = "Adam"

# Here, we're converting the string into a list for manipulation
letter_list = [char for char in name]

# Converting the list back to a string by joining each character together
output = "".join(letter_list)

# print(output)
#----------------------------------------------------------------------------------------------------------
# Another example is doubling numbers inside a given range
doubled_num_list = [n*2 for n in range(1, 100)]

# print(doubled_num_list)
#----------------------------------------------------------------------------------------------------------
name_list = ["adam", "madison", "alex", "dor", "alon"]

# Here we're doing much of the same thing as before, but now we're adding an if statement that adds the name
# if it's length is equal to 4.
four_letter_names = [name for name in name_list if len(name) == 4]

# print(four_letter_names)
#----------------------------------------------------------------------------------------------------------
# Here we create a list which stores capitalized names from the original name list
capitalized_names = [name.title() for name in name_list]

# print(capitalized_names)
#----------------------------------------------------------------------------------------------------------
