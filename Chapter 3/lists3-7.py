dinner_guests = ['george', 'tina', 'robin']

dinner_guests.insert(0, 'donna')
dinner_guests.insert(2, 'shellie')
dinner_guests.append('garret')


print("\nIt looks like I can only invite 2 people to dinner.")

removedguests = dinner_guests.pop(2)

print (f"\nHey {removedguests.title()}. We do not have enough room for you to show up for dinner.")

removedguests = dinner_guests.pop(0)

print (f"\nHey {removedguests.title()}. We do not have enough room for you to show up for dinner.")

removedguests = dinner_guests.pop(-1)
 
print (f"\nHey {removedguests.title()}. We do not have enough room for you to show up for dinner.")

removedguests = dinner_guests.pop(-1)

print (f"\nHey {removedguests.title()}. We do not have enough room for you to show up for dinner.")

print (f"\nHey {dinner_guests [0].title()}, {dinner_guests [1].title()}.  See you two at 6pm.")

print (dinner_guests)

del dinner_guests

print (dinner_guests)