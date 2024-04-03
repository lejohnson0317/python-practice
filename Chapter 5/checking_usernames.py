current_users = ['admin', 'LJohnson', 'jdoe', 'rreynolds', 'sjohnson']
new_users = ['gjohnson', 'ljohnson', 'dturner', 'saywhat', 'toomuch']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}. This user account already exists!")
    else:
        print(f"Great {new_user}. You have successfully created a new username.")