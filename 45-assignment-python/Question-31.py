# Array of usernames (Initially populated with users)
usernames = ['alice', 'bob', 'admin', 'charlie', 'david']

# Check if the list is empty
if not usernames:
    print("We need to find some users!")
else:
    # Loop through the list of usernames and greet each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")

# Now, remove all usernames and check again
usernames.clear()  # Removes all users from the list

# Check if the list is empty
if not usernames:
    print("We need to find some users!")
