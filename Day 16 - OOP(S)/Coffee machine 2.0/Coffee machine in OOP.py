# Same requirements as before but this time USING OBJECTS YEAH BABY

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
menu_item = MenuItem
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    # Main program functionality

    choice = input(f"Choose {menu.get_items().title()}\n")
    # Ask for user input

    if choice == "report":
        coffee_machine.report()
        # Reports status
        main()
        # Returns to start

    elif choice == "money report":
        money_machine.report()
        # Reports money amount
        main()
        # Returns to start

    elif choice == "off":
        print("Goodbye!")
        # Exists function

    else:
        drink = menu.find_drink(choice)
        # Assigns drink object based on chosen drink

        if coffee_machine.is_resource_sufficient(drink):
            # Checks if there are enough resources for chosen coffee type
            if money_machine.make_payment(drink.cost):
                # Asks user to insert coins and checks payment

                coffee_machine.make_coffee(drink)
                # If transaction successful make drink and subtract resources

                main()
                # Return to main function
        else:
            main()
            # If payment failed, return to main function


main()
# That was a difficult one to understand :(
