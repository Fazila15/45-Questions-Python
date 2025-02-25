# Function to describe a city and its country
def describe_city(city, country='Pakistan'):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city('Karachi')  # Uses default country (Pakistan)
describe_city('Lahore')   # Uses default country (Pakistan)
describe_city('New York', 'USA')  # Uses a custom country (USA)
