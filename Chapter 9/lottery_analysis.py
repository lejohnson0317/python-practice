
from random import choice

def get_winning_ticket(possibilities):
    winning_ticket = []
    
    while len(winning_ticket) < 4:
        draw = choice(possibilities)
        """Make sure we don't duplicate a drawn possibility"""
        if draw not in winning_ticket:
            winning_ticket.append(draw)
    
    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    
    return True

def make_random_ticket(possibilities):
    ticket = []

    while len(ticket) < 4:
        draw = choice(possibilities)
        """Make sure we don't duplicate a drawn possibility"""
        if draw not in ticket:
            ticket.append(draw)
    
    return ticket

possibilities = (3, 16, 42, 8, 19, 47, 38, 5, 26, 33, 'g', 'e', 'p', 'z', 't')
winning_ticket = get_winning_ticket(possibilities)
print(winning_ticket)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"It only took '{plays}' tries to win!")
else:
    print("Tried {plays} times, without pulling a winner.")