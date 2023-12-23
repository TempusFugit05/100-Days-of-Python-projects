from random import randint

#----------------------------------------------------------------------------------------------------------
# It is possible to do much of the same things we did with list comprehension but with dictionaries
name_list = ["adam", "syoma", "alisa", "alon", "dror"]

# Here we are taking each name in the list as a key and assigning a value based on ra random number
name_dict = {name: randint(1, 100) for name in name_list}

# print(name_dict)
#----------------------------------------------------------------------------------------------------------
# This creates a new dictionary that contains the key, value pairs only of the people who got a grade
# greater than 60

# * The item() method creates a list of tuples with the keys and values
passed_students = {name: grade for (name, grade) in name_dict.items() if grade > 60}

print(passed_students)
#----------------------------------------------------------------------------------------------------------
