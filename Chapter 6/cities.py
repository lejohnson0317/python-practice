cities = {
  "Tokyo": {
    "country": "Japan",
    "population": 37.433,  # Assuming population in millions
    "fact": "Tokyo is the most populous metropolitan area in the world."
  },
  "London": {
    "country": "United Kingdom",
    "population": 8.9,  # Assuming population in millions
    "fact": "London is home to the iconic Buckingham Palace."
  },
  "Paris": {
    "country": "France",
    "population": 2.1,  # Assuming population in millions
    "fact": "The Eiffel Tower was built for the 1889 World's Fair."
  }
}

for location, city in cities.items():
    print(f"{location.title()} is located in {city['country'].title()} and has a population of {city['population']} million.  {city['fact']}")