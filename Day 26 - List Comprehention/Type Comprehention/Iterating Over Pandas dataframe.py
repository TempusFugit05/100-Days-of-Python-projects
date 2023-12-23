import pandas

# Creating a dictionary
test_dict = {
    "letters": ["a", "b", "c", "d"],
    "numbers": [1, 2, 3, 4]
}

# Creating a dataframe
test_dframe = pandas.DataFrame(test_dict)

# Integrating over each row and saving it as a variable
for (index, row) in test_dframe.iterrows():

    # Printing the number attribute of the row (Remember, this is a pandas row object!)
    print(row.numbers)