############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# # Nothing will be printed since the range function does not include 20.
# # Therefore, the if statement will never get triggered.
# #  It is important to describe the problem at hand. In this case, the line "You got it" does not get printed.

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # The index of the given list starts at 0 and goes up to 5.
# # Here, the random function is between 1 and 6, meaning that the function might be out of range when trying to access the list.
# # Reproducing the problem can help in finding out how to fix it.
# # In this case, we get a clue as to what went wrong since we get an out of range error.

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millennial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# # The code does not account for the year 1994. The if statement ends with 1993 and the elif starts with 1995.
# # It is useful to sometimes play computer and go step by step in figuring out what went wrong.

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# # Fix the errors the editor highlights lol
# # In this case, the print statement is not indented properly and thus, the if statement will remain empty, giving out an error.
# # There is an additional error here, being that the type of the age is string and in the if statement we're comparing it to an integer, resulting in an error.
# # Lastly, the print statement is not converted to an fstring meaning that it will be printed as is. The if statement also does not account for the input being 18.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # The mistake here is that instead of equating word_per_page to an input, we're comparing it to the input, meaning the variable stays at 0.
# # It is important to print out problematic variables to figure out their behaviour and fix the problem.

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
# # In this case, during the for loop, the new_item variable gets overwritten during every cycle, meaning only on the last cycle will it be added to the b_list.

"""
Final tips:
* Taking a break can help in getting a different view of the problem and finding a solution.
* Asking someone for help.
* Running the program often is useful in catching bugs early.
* Asking for help on stack overflow when there's no other way could be useful. I guess asking ChatGPT can also help lol
"""