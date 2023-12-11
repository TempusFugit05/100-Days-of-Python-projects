dictionary = {
    "Human": "A monkey (basically)",
    "Poopoo Kaka Fart": "A funny word",
    "Doo Doo": "RAAAAAAAAA!",
    123: "A number",
}
# Dictionaries are divided into Keys and Values (Key: Value, etc.)
# The keys in dictionaries can be of different data types
print(dictionary["Human"])
# Accessing the dictionary

dictionary["Amongus"] = "Sus"
print(dictionary["Amongus"])
# Adding a new item to the dictionary

Empty_dictionary = {}
# It's possible to create an empty dictionary

"""
print(dictionary)
dictionary = {}
print(dictionary)
# It's possible to wipe an existing dictionary
"""

dictionary["Human"] = "A big fatty monkey"
print(dictionary["Human"])
# It's possible to edit an existing item in a dictionary
# If there's no item matching the name, a new item will be created

for item in dictionary:
    print(item)
# In this instance, the program will print only the key.
# To print out the value we would write print(dictionary[item])