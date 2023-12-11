global_var = 1
# This is a global variable, and it can be accessed anywhere in the code.

def func():
    global_var = 2
    print(global_var)
func()
print(global_var)

# In this case, the variable inside the function is defined separately from the global one

def func2():
    #print(global_var)
    # With this configuration, the program will error since, the function has no access to the global one, and thus, it
    # will be considered as undefined.
    global global_var
    # To use the global variable, we have to use the global statement.
    # It is however, not recommended since this solution is prone to bugs.
    print(global_var)
    global_var = 2
    print(global_var)
func2()

PI = 3.14
# Constant variables are better used as globals since they shouldn't change and therefore won't make problems
# It is also recommended to name them in upper case to differentiate them from regular variables
