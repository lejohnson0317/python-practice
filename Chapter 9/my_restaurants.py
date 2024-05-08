from restaurant import Restaurant

american_restaurant = Restaurant('The Big Cheese', 'American')
american_restaurant.describe_restaurant()
american_restaurant.open_restaurant()
american_restaurant.set_number_served(1_234)

italian_restaurant = Restaurant('The Big Gambino', 'Italian')
italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()
italian_restaurant.set_number_served(3_456)

chinese_restaurant = Restaurant('The Big Chink', 'chinese')
chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()
chinese_restaurant.set_number_served(5_875)