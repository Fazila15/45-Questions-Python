# Function to print the names of magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Function to add "the Great" to each magician's name
def make_great(magicians):
    great_magicians = []  # Create a new list to store the modified names
    for magician in magicians:
        great_magicians.append(f"{magician} the Great")
    return great_magicians  # Return the modified list

# Array of magician names
magicians_list = ['David Copperfield', 'Harry Houdini', 'Derren Brown', 'Penn & Teller']

# Create a copy of the original list and modify the copy
great_magicians_list = make_great(magicians_list)

# Print the original list (unchanged)
print("Original magicians:")
show_magicians(magicians_list)

# Print the modified list
print("\nModified magicians:")
show_magicians(great_magicians_list)
