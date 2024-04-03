#Testing for equality
drinking_age = 21
your_age = 19

if your_age >= drinking_age:
    print("You are old enough to drink.")
else:
    print("You are not old enough to drink.")

#Testing for equality with strings
motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki']
my_bike = 'bmw'

if my_bike in motorcycles:
    print(f"You ride a {my_bike} and it's in the approved list.")
elif my_bike != motorcycles:
    print(f"Sorry, you ride a {my_bike} which is not on the approved list.")
