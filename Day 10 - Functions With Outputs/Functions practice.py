"""def test_func():
    result = 6*21
    return result
print(test_func())
# It is possible to return a value of a variable inside a function using the return statement
"""
'''
def new_test_func(f_name, l_name):
    f_name = list(f_name)
    f_name[0] = f_name[0].upper()
    f_name = ''.join(f_name)
    l_name = list(l_name)
    l_name[0] = l_name[0].upper()
    l_name = ''.join(l_name)
    return f_name, l_name

    f_name_string = 
    for letter in f_name:
        f_name_string += letter
    f_name = f_name_string
    return f_name"""
# One way of achieving this is by creating a for loop to add all the letters onto a string
# A simpler way to do this is by using the .join() func
print(new_test_func("banana","boba milk"))
'''
# An even easier way to do this is by using the title() method o_0
# This function works by converting EVERY word in a string into upper case. Neat!
def new_new_test_func(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name, l_name
print(new_new_test_func("banana","boba milk"))
