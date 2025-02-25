# Defining a class for Cities
class City:
    def __init__(self, name, country, population):
        self.name = name
        self.country = country
        self.population = population

    def display_info(self):
        print(f"City: {self.name}")
        print(f"Country: {self.country}")
        print(f"Population: {self.population}")
        print("--------------")

# Creating city objects
city1 = City("Tokyo", "Japan", 13929286)
city2 = City("Paris", "France", 2148327)
city3 = City("New York", "USA", 8419600)
city4 = City("Sydney", "Australia", 5312163)
city5 = City("Cape Town", "South Africa", 433688)

# Storing the city objects in a list
cities = [city1, city2, city3, city4, city5]

# Printing information about each city
for city in cities:
    city.display_info()
