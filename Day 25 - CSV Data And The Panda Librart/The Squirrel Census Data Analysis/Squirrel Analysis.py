import pandas

# Read the csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the fur color rows
squirrel_color = data["Primary Fur Color"]

# Find the amount of rows containing the color keywords
gray_fur = len(data[squirrel_color == "Gray"])
black_fur = len(data[squirrel_color == "Black"])
cinnamon_fur = len(data[squirrel_color == "Cinnamon"])

# Create a new dictionary that contains the colors and their amounts
fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Amount": [gray_fur, cinnamon_fur, black_fur]
}

# Convert dictionary to dataframe
df = pandas.DataFrame(fur_dict)

# Create new csv file
df.to_csv("Colors")