# A few ways to manipulate strings and files in python

# Removes spaces at the beginning and end of string
test_string = "    test 1    "
print(test_string.strip())

# Replaces one string (or a part of a string) with another
test_string = "I love pineapples on pizza"
print(test_string.replace("love", "HATE"))