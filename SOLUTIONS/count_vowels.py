# Function: count_vowels (2 points)

# Write a Python function named count_vowels that takes a string text as input and returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity.

# Creating the Function
def count_vowels(text):
    # Request input from User
    # text = input("Please Enter the Text You wish to Count Vowels :  ")
    # The Set of Vowels
    vowels = "aeiou"
    # Counting the Vowels
    vowel_count = 0
    # Iterating through the text
    for vowel in text.lower():
        if vowel in vowels:
            # Increamenting the count
            vowel_count += 1
    # Printing the results
    if vowel_count == 1:
        print(f"The text '{text}' contains {vowel_count} Vowel.")
    elif vowel_count > 1:
        print(f"The text '{text}' contains {vowel_count} Vowels.")
    else:
        print(f"The text '{text}' contains no Vowels.")

count_vowels("Eric")