# Define some variables for testing
car = "subaru"
fruit = "apple"
age = 25
height = 170
city = "Paris"
is_student = True
languages = ["English", "Spanish", "French", "German"]

# Equality and Inequality with strings

# Test 1: Testing equality of strings (True)
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')  # True

# Test 2: Testing inequality of strings (False)
print("\nIs fruit != 'banana'? I predict False.")
print(fruit != 'banana')  # False

# Tests using the lower case function

# Test 3: Testing equality after converting to lowercase (True)
print("\nIs 'paris'.lower() == city.lower()? I predict True.")
print('paris'.lower() == city.lower())  # True

# Test 4: Testing inequality after converting to lowercase (False)
print("\nIs 'PARIS'.lower() != city.lower()? I predict False.")
print('PARIS'.lower() != city.lower())  # False

# Numerical tests (equality, inequality, greater than, less than, >=, <=)

# Test 5: Testing equality of numbers (True)
print("\nIs age == 25? I predict True.")
print(age == 25)  # True

# Test 6: Testing inequality of numbers (False)
print("\nIs age != 30? I predict False.")
print(age != 30)  # False

# Test 7: Testing greater than comparison (True)
print("\nIs age > 20? I predict True.")
print(age > 20)  # True

# Test 8: Testing less than comparison (True)
print("\nIs height < 180? I predict True.")
print(height < 180)  # True

# Test 9: Testing greater than or equal to comparison (True)
print("\nIs height >= 170? I predict True.")
print(height >= 170)  # True

# Test 10: Testing less than or equal to comparison (False)
print("\nIs age <= 20? I predict False.")
print(age <= 20)  # False

# Tests using "and" and "or" operators

# Test 11: Using 'and' operator (True)
print("\nIs age > 18 and height < 180? I predict True.")
print(age > 18 and height < 180)  # True

# Test 12: Using 'or' operator (True)
print("\nIs age > 30 or city == 'Paris'? I predict True.")
print(age > 30 or city == 'Paris')  # True

# Test 13: Using 'and' operator (False)
print("\nIs age < 20 and height > 180? I predict False.")
print(age < 20 and height > 180)  # False

# Test 14: Using 'or' operator (False)
print("\nIs city == 'London' or age == 30? I predict False.")
print(city == 'London' or age == 30)  # False

# Test whether an item is in a list (True)

# Test 15: Checking if an item is in the list (True)
print("\nIs 'English' in languages? I predict True.")
print('English' in languages)  # True

# Test whether an item is not in a list (True)

# Test 16: Checking if an item is not in the list (True)
print("\nIs 'Chinese' not in languages? I predict True.")
print('Chinese' not in languages)  # True
