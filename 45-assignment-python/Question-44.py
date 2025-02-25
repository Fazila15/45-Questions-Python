# Function to summarize the sandwich order
def make_sandwich(*items):
    print("\nYou are ordering a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Enjoy your sandwich!\n")

# Calling the function with different numbers of arguments
make_sandwich('lettuce', 'tomato', 'turkey')
make_sandwich('cheese', 'ham', 'pickles', 'onions')
make_sandwich('avocado', 'chicken', 'spinach')
