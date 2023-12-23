import csv

# This is the regular way to read a csv file
# with open("weather_data.csv") as file:
#     contents = file.read()
#     contents = list(contents.split(sep="\n"))
#     print(contents)

"""with open("weather_data.csv") as file:
    # The csv library allows to more easily read csv files
    contents = csv.reader(file)

    # # This method allows for line by line reading of the csv file
    # for row in contents:
    #     print(row)

    # Define temperature list
    data_list = []

    # Define which data to look for
    data_type = "temp"

    # Loop over each row
    for row in contents:

        # Loop for each word in row
        for word in row:

            # If word is temp, save its index
            if word == data_type:
                index = row.index(word)

        # Save the correct strings in a list
        data_list.append(row[index])

    # Remove data name from list
    data_list.remove(data_type)

    # Convert data from string to int
    for item in data_list:
        data_list[data_list.index(item)] = int(item)

    print(data_list)
    
    While this method will work with other data types, it is inefficient and long
    """

# A simpler way to do this will be like this:
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temp_data = []

    # Iterate for each row in the file
    for row in data:

        # Check if the value in the row isn't the title of the column
        if row[1] != "temp":

            # Convert the value to integer and add it to list
            temp_data.append(int(row[1]))

    print(temp_data)
