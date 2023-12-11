def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}


def operation(user_number_a):
    user_operation = input("Choose what operation to do ")
    user_number_b = float(input("Choose a number "))
    result = operations[user_operation](a = user_number_a, b = user_number_b)
    print(f"{user_number_a} {user_operation} {user_number_b} = {result}")
    if input("Do another operation?").lower() == "yes" or "y":
        operation(result)
    else:
        print(result)


operation(float(input("Choose a number ")))