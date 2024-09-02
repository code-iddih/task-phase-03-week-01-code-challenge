# Object-Oriented Programming: Class Creation (2 points)

# Define a Python class named Car with the following attributes: make, model, year. Implement a method named display_info that prints out the car's information.

# Defining the Class
class Car:

    # The Constructor
    def __init__( self , make , model , year): # Initializing the attributes
    # Assigning values to the instance's attributes
        self.make = make
        self.model = model
        self.year = year

    # Method to display the car's information 
    def display_info( self ):
        # Listt of Tuples to hold the attributes
        attributes = [(" Make " , self.make) , (" Model " , self.model) , (" Year " , self.year)]
        
        # Setting up a title
        print("Your Car's Information is as Follows :")
        
        # Looping through thhe List
        for key , value in attributes:
            # printing the Keys and the Valuse
            print(f"{key} : {value}")

car_detail = Car(" Mitsubishi " , " C740 " , 2023)
# Displaying the car details
car_detail.display_info()