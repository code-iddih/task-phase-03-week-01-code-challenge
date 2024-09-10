# Sequences: Sort List of Tuples (1 point)

# Given a list of tuples where each tuple contains a name and an age, write a Python function named sort_by_age that sorts the list of tuples by age in ascending order.

# Creaing the Function
def sort_by_age(detail):

    # Sorting the list of Tuples by Age
    details.sort(key = lambda x : x[1]) # Since age is stored in index 1 of every tuple

    # Printing the Solutiion
    for detail in details: # So that the ouutput prints vertically
        print(detail)

    # Initializingg a List of tuples
details = [(" Eric " , " 40 ") , (" Ayim " , " 28 ") , (" Centrine " , " 20 ") , (" George " , " 33 ") ]
# Calling thhe Function
sort_by_age(details)