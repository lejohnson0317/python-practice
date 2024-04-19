
def city_country(city, country):
    """Format city country as follows 'City, Country'"""
    format_name = f"{city}, {country}"
    return format_name.title()

places = city_country('stuttgart', 'germany')
print(places)
places = city_country('london', 'united')
print(places)
places = city_country('paris', 'france')
print(places)