cars = ['bmw', 'audi', 'toyota', 'subaru']

print ("Here is the original list:")
print (cars)

print ("\nHere is the sorted list:")
print (sorted(cars))

print ("\nHere is the reverse sorted list:")
print (sorted(cars,reverse=True))  # This line will sort the list

print ("\nHere is the original list again:")
print (cars)

print("Here is a different method for printing reverse order.\n")
cars.reverse()
print(cars)

print(f"\nThere are {len(cars)} car models in this list.")