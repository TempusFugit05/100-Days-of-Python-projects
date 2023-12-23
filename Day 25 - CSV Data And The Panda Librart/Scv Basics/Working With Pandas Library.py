import pandas

# Reading the csv file using pandas
data = pandas.read_csv("weather_data.csv")

# Printing the temperature column
"""print(data["temp"])"""

# It's also possible to convert the data to a dictionary type
data_as_dictionary = data.to_dict()
# print(data_as_dictionary)

# It's also possible to convert a specific column to the list of its values
"""temp_list = data["temp"].to_list()
print(temp_list)"""

# Finding the average of temperatures
"""total_temp = 0

# Finding the total of temperatures
for temp in temp_list:
    total_temp += temp

# Finding the average
average_temp = round(total_temp/len(temp_list), 2)

print(f"{average_temp} C")"""

# Another way to find the average
"""average_temp = round(sum(temp_list)/len(temp_list), 2)
print(average_temp)"""

# An even shorter way to do this using the pandas library
"""average_temp = data["temp"].mean()
print(average_temp)"""

# Finding the highest temperature in the file using panda methods
"""print(data["temp"].max())"""

# Printing the conditions for example, can be done using the name of the column as a string
"""print(data["condition"])"""

# Alternatively we can achieve the same result using an attribute
"""print(data.condition)"""

# If we want to get hold of a row instead of a column, we have to access the data variable, and find inside it
# the day in the days row which is equal to Monday
"""print(data[data["day"] == "Monday"])"""

# if we want to find the row in which we have the maximum temperature of the week, for example, we can do it like so:
"""print(data[data.temp == data.temp.max()])"""

# Here we can also create variables to be used as specific data inside the file
# For example, here we have a variable which stores the entire row in which the day is monday
monday = data[data.day == "Monday"]

# And we can also access a specific attribute of that row
print(monday.temp)

# If we want to convert Celsius to Fahrenheit, the formula would be F = 1.8*C + 32

# We would have to specify that we want the temperature and index 0 to only get the value.
# Otherwise, we'd also get some other information about the piece of data like so: "Name: temp, dtype: int64"
monday_temp = monday.temp[0]
print(f"{monday_temp}C would be {round(monday_temp*1.8 + 32, 2)}F")

# Creating a dataframe using the library
dataframe = pandas.DataFrame(data_as_dictionary)

# It is even possible to create a csv file using the dataframe
dataframe.to_csv("back_to_csv.csv")