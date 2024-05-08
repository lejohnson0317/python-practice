class Restaurant():
    """This is a class to define available restaurants."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        number_served = 0

    def describe_restaurant(self):
        """Describe the type of restaurant which will include name and cuisine"""
        print(f'\nThe restaurant name is "{self.restaurant_name}".')
        print(f'The cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        """Print a message that the restaurant is open."""
        print(f'"{self.restaurant_name}" is open.')

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = str(number_served)
        print(f'The number of customers served is {self.number_served}.')

class IceCreamStand(Restaurant):
    """This is a class describing a specific restaurant using the Restaurant class."""
    def __init__(self, restaurant_name, cuisine_type = "Ice Cream"):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def describe_flavors(self):
        """Print a list of flavors."""
        print("The flavors are: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}.")


big_ice = IceCreamStand('The Big Ice Cream')
big_ice.flavors = ['vanilla', 'chocolate', 'strawberry']

big_ice.describe_restaurant()
big_ice.describe_flavors()