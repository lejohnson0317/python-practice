def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('larry', 'johnson', location='grapevine',field='information technology',hobby='motorcycles',dob='6/22/1967')
print(user_profile)