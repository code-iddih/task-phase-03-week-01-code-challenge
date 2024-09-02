# Function: apply_decorator (1 point)

# Write a Python function named apply_decorator that takes a function func as input and applies a decorator named decorator_func. The decorator should simply print "Decorator Applied" before calling the original function.

# Creating the Decorator Function
def apply_decorator( func ):
    def wrapper(): # Adds the Extra Behaviour
        print("Decorator Applied")
        func() # Calling the Original Function
    return wrapper

@apply_decorator # Applying the decorator Function
def decorator_func(): # The Original Function
    print("I am now Called!")

# Calling the Function
decorator_func()
