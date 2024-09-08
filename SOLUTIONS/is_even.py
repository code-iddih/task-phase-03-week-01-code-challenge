# Function: is_even (2 points)

# Write a Python function named is_even that takes a single parameter number and returns True if the number is even, and False otherwise.

# Creating the function
def is_even( number ):
    # Checks if the number is EVEN
    if number < 0:
        print("Please Use a Positive Integer.")
    return number % 2 == 0 


# Calling the Function
print(is_even(3))