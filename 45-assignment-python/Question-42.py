# Function to print the names of magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# Function to add "the Great" to each magician's name
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"

# Array of magician names
magicians_list = ['David Copperfield', 'Harry Houdini', 'Derren Brown', 'Penn & Teller']

# Modifying the array by adding "the Great" to each name
make_great(magicians_list)

# Calling the function to print the modified list
show_magicians(magicians_list)
