#COSC 1104 – Assignment 1
# Author: Arjun Bindhu Suresh
# Date: October 2024
# Description: This program checks if a number is prime, finds the prime number before and after, and lists divisors if it's not prime.


# Function to check if a number is prime
def prime(n):
    if n < 2:  
        return False
    for i in range(2, n):
        if n % i == 0:  
            return False
    return True  

# Function to find the largest prime number before the given number
def previous_prime(n):
    for i in range(n-1, 1, -1):  
        if prime(i):
            return i
    return None  

# Function to find the next prime number after the given number
def next_prime(n):
    i = n + 1  
    while True:  
        if prime(i):
            return i
        i += 1

# Function to get a positive whole number from the user
def get_positive_number():
    while True:
        user_input = input("\nPlease enter a positive whole number: ")
        if user_input.isdigit():  
            return int(user_input)
        else:
            print("\nAlert!.\nThe number you have entered is not a positive whole number. \nTry again.")

def main():
    print("\nWelcome to the Prime Number Checker!\n")
    number = get_positive_number()

    # Check if the number is prime
    if prime(number):
        print(f"{number} is a prime number.")
    else:
        # Find and display the divisors
        divisors = [i for i in range(2, number) if number % i == 0]
        print(f"The number you have entered {number} is not a prime number.\nIts divisors are: {divisors}")

    # Find and display the previous and next prime numbers
    previous = previous_prime(number)
    next = next_prime(number)

    if previous:
        print(f"The prime number before {number} is {previous}.")
    else:
        print(f"There is no prime number before {number}.")

    print(f"The prime number after {number} is {next}.")

    input("\nPress Enter to exit the program...")

if __name__ == "__main__":
    main()
