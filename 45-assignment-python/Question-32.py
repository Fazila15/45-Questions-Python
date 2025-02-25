# List of current usernames
current_users = ['alice', 'bob', 'admin', 'charlie', 'david']

# List of new usernames
new_users = ['john', 'alice', 'bob', 'Eve', 'CHARLIE']

# Loop through the new_users list and check if each username has already been used
for new_user in new_users:
    # Check if the new username already exists in the current_users list (case insensitive)
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a new one.")
    else:
        print(f"Username '{new_user}' is available.")
