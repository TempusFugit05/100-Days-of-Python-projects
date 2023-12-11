import prettytable
# Importing prettytable package to make a table in ascii

table = prettytable.PrettyTable()
# Assigning prettytable class to table variable

table.add_column("Test", ["1", "2", "3"])
# Adding a column using the add_column() method and assigning table name and data to be displayed inside

table.add_column("Success", ["Yes", "No", "Yes"])
# Adding a second column

table.align["Test"] = "l"
table.align["Success"] = "l"
# Changing the attributes of both of the columns to align them to the left

print(table)
