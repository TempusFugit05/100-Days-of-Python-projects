import random
number = random.randint(1, 100)

def prime_checker(number):
    is_prime = True
    # The default is that the number is a prime
    i = 2
    # index variable
    while is_prime and i < number:
        # This loop breaks once the number is proven to not be a prime or once the index reaches the number itself
        # The loops works by checking if the given number can be divided by any number between 2 and itself (not including)
        if number % i == 0:
            is_prime = False
        print(f"{number}%{i}={number%i}")
        i += 1
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

prime_checker(number)