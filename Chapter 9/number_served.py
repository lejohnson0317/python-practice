class Restaurant():
    """This is a class to define available restaurants."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the type of restaurant which will include name and cuisine"""
        print(f'The restaurant name is "{self.restaurant_name}".')
        print(f'The cuisine type is {self.cuisine_type}.')

    def open_restaurant(self):
        """Print a message that the restaurant is open."""
        print(f'"{self.restaurant_name}" is open.')

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served
        print(f'The number of customers served is {self.number_served:,}.')

    def increment_number_served(self, more_served):
        """Incrementing the number served"""
        self.number_served += more_served
        print(f'The number of customers served is {self.number_served:,}.')


american_restaurant = Restaurant('The Big Cheese', 'American')
american_restaurant.describe_restaurant()
american_restaurant.open_restaurant()
american_restaurant.set_number_served(1_234)
american_restaurant.increment_number_served(100)

italian_restaurant = Restaurant('The Big Gambino', 'Italian')
italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()
italian_restaurant.set_number_served(3_456)
italian_restaurant.increment_number_served(150)

chinese_restaurant = Restaurant('The Big Chink', 'chinese')
chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()
chinese_restaurant.set_number_served(5_875)
chinese_restaurant.increment_number_served(200)