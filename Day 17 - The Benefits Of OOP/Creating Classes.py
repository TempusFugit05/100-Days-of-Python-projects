class Test:
    # Defining a class
    # Every word should be capitalized in the class name (Called PascalCase)

    # pass
    # # A placeholder statement that doesn't do anything when the code is executed

    def __init__(self, success):
        # To assign starting attributes to a class we use __init__ to initialize them

        print("Trololo")

        self.success = success
        # Creating an attribute


test1 = Test(True)
# Defining a Test object
# When a class is being called, the initialization function is called as well
# It's also possible to pass values to be assigned to the attributes in the initialization function

test1.number = 69
# Assigning a new attribute to the Test object

print(test1.number, test1.success)


class Car:
    def __init__(self, car_seats):
        self.car_seats = car_seats
        # Creating a car seats attribute

    def enter_race_mode(self):
        self.car_seats = 2
        # Creating a race mode method


car = Car(5)

print(car.car_seats)
car.enter_race_mode()
print(car.car_seats)