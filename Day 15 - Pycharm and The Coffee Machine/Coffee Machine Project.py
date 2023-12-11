from coffee_info import MENU
menu = MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25


def report():
    """
    Prints how much water, milk, coffee and money is in the machine
    :return:
    """
    global resources
    print(f"Water: {resources["water"]} ml\n"
          f"Milk: {resources["milk"]} ml\n"
          f"Coffee: {resources["coffee"]} grams\n"
          f"Money: {resources["money"]}$")
    # prints resources


def insert_coins(cost, choice):
    """
    Handles inputting money into the machine
    :return:
    """
    global penny, nickel, dime, quarter, menu
    print(f"{choice.title()} costs {cost}$")
    num_penny = penny * int(input("How many pennies "))
    num_nickel = nickel * int(input("How many nickels "))
    num_dime = dime * int(input("How many dimes "))
    num_quarter = quarter * int(input("How many quarters "))
    # How many coins of each type

    total_money = round(num_penny + num_nickel + num_dime + num_quarter, 3)
    # Calculates total money amount

    if total_money >= cost:
        resources["money"] += cost
        resources["water"] -= menu[choice]['ingredients']['water']
        resources["milk"] -= menu[choice]['ingredients']['milk']
        resources["coffee"] -= menu[choice]['ingredients']['coffee']
        print(f"Your change is {total_money-cost}$")
        print(f"Your {choice.title()} is HOT AND READY!")
        report()
        main()
        # If enough money was inserted, add cost to resources, subtracts ingredients and give change
    else:
        print(f"Not enough money...\nREFUNDED {total_money}$\nLet's try that again...")
        main()
        # If not enough money was inserted, try again
    return total_money


def not_enough_resources(choice):
    global menu, resources

    if menu[choice]['ingredients']['water'] > resources['water']:
        print(f"Sorry, there's not enough water to fill your order!\n"
              f"Order requires {menu[choice]['ingredients']['water']} ml of water.\n"
              f"Only {resources["water"]} ml of water is available")
        # Prints error for not enough water

    elif menu[choice]['ingredients']['milk'] > resources['milk']:
        print(f"Sorry, there's not enough milk to fill your order!\n"
              f"Order requires {menu[choice]['ingredients']['milk']} ml of milk.\n"
              f"Only {resources["milk"]} ml of milk is available")
        # Prints error for not enough milk

    else:
        print(f"Sorry, there's not enough coffee to fill your order!\n"
              f"Order requires {menu[choice]['ingredients']['coffee']} grams of coffee.\n"
              f"Only {resources["coffee"]} grams of coffee are available")
        # Prints error for not enough coffee

    main()
    # Returns to main function


def main():

    global menu
    choice = str(input("Choose coffee: Latte, Espresso or Cappuccino\n")).lower()
    # Initial prompts

    if choice == "report":
        report()
        main()
        # Shows machine report and restarts prompts

    elif choice == "off":
        print("Shutting down for maintenance...\nSee ya!")
    # Ends program when machine is turned off

    elif choice == "water":
        if menu[choice]["ingredients"]["water"] <= resources["water"]:
            resources["water"] -= menu[choice]["ingredients"]["water"]
            print("Stay hydrated homie!")
            main()
            # Secret water menu item
        else:
            not_enough_resources(choice)

    elif menu[choice]['ingredients']['water'] <= resources['water'] and menu[choice]['ingredients']['milk'] <= resources['milk'] and menu[choice]['ingredients']['coffee'] <= resources['coffee']:
        insert_coins(choice=choice, cost=menu[choice]['cost'])
        # Checks if machine has sufficient resources before asking for money

    else:
        not_enough_resources(choice)
        # If there are not enough resources for selected coffee, restarts prompts


main()