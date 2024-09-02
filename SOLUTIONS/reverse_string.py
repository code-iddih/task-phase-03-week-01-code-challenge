# Function: reverse_string (2 points)

# Write a Python function named reverse_string that takes a string text as input and returns the reversed version of that string.

# Creating the Function
def reverse_string():
    # Request input from User
    text = input("Please Enter the Text You wish to reverse :  ")
    # Begin from the end and end at the beginning, one step backwards
    reversed_text = text[::-1]
    # Printing the new Text
    print(f"When the Text '{text}' is reversed, it becomes : {reversed_text} ")

# Calling the Function
reverse_string()