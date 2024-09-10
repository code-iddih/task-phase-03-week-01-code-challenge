# Sets and Dictionaries: Merge Dictionaries (1 point)

# Write a Python function named merge_dicts that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values should be summed up.

# Creating the function
def merge_dicts(dict1, dict2):
# Initializing two dictionaries

    # Creating a copy of thhe 1st dictioanry
    merged_contributions = dict1.copy()

    for key , value in dict2.items():
        if key in merged_contributions: 
            merged_contributions[key] += value # Summing the values if keys are the same
        else:
            merged_contributions[key] = value # If the key doesnt exist, it will adds it

    # Printing the results
    print(merged_contributions)


    # Dictionary 1
contributions_from_church_a = {" Food " : 2000 , " Water " : 500 , " Clothes " : 4000 , " Transport " : 2500}
    # Dictioanry 2
contributions_from_church_b = {" Toiletries " : 2300 , " Food " : 1000 , " Water " : 700 , " Clothes " : 4000 , " Transport " : 1700}
# Calling the Function
merge_dicts(contributions_from_church_a , contributions_from_church_b)