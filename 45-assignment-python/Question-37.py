# Function to make a shirt with default size and message
def make_shirt(size='L', message='I love TypeScript'):
    print(f"The shirt is size {size} and has the message: '{message}'.")

# Call the function with the default size and message
make_shirt()

# Call the function with a different size but default message
make_shirt('M')

# Call the function with a custom size and message
make_shirt('S', 'Coding is life!')
