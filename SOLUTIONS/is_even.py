# Function: is_even (2 points)

# Write a Python function named is_even that takes a single parameter number and returns True if the number is even, and False otherwise.

# Creating the function
def is_even( number ):
    # Checks if the number is EVEN
    if number < 0:
        print("Please Use a Positive Integer.")
    elif number % 2 == 0 :
        print(f"The Number {number} is EVEN.")
    # if the number is not EVEN then it is ODD
    else : 
        print(f"The Number {number} is ODD.")

# Calling the Function
is_even(3)