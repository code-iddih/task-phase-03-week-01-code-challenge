# Sets and Dictionaries: Merge Dictionaries (1 point)

# Write a Python function named merge_dicts that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values should be summed up.

# Creating the function
def merge_dicts():
# Initializing two dictionaries
    # Dictionary 1
    contributions_from_church_a = {" Food " : 2000 , " Water " : 500 , " Clothes " : 4000 , " Transport " : 2500}
    # Dictioanry 2
    contributions_from_church_b = {" Toiletries " : 2300 , " Food " : 1000 , " Water " : 700 , " Clothes " : 4000 , " Transport " : 1700}

    # Creating a copy of thhe 1st dictioanry
    merged_contributions = contributions_from_church_a.copy()

    for key , value in contributions_from_church_b.items():
        if key in merged_contributions: 
            merged_contributions[key] += value # Summing the values if keys are the same
        else:
            merged_contributions[key] = value # If the key doesnt exist, it will adds it

    # Printing the results
    print(merged_contributions)

# Calling the Function
merge_dicts()