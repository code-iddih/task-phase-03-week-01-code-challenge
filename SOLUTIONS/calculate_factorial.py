# Function: calculate_factorial (2 points)

# Write a Python function named calculate_factorial that takes a non-negative integer n as input and returns the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

# Creating the Function
def calculate_factorial(n):
    # Request input from User
    # n = int(input("Please Enter a Number to Calculate its Factorial! :  "))
    # Initializing the Factorial variable to 1
    factorial = 1
    # Checking if the number is a Positive Integer
    if n < 0:
        print(f"Invalid!! Please Enter a Positive Integer.")
    elif n == 0 or n == 1:
        return 1
    else:
        # iterating through the numbers less thaan it
        factorial = 1
        for i in range (2, n +1):
            # Multiplying by current value
            factorial *= i
        return factorial

print(calculate_factorial(5))