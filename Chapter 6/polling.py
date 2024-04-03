favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

users =  ['jen', 'sarah', 'ed', 'larry']

for user in users:
    if user in favorite_languages.keys():
        print(f"Hi {user.title()}. Thank you for taking the poll!")
    else:
        print(f"Hi {user.title()}. Please take the language poll.")