# Array of usernames
usernames = ['alice', 'bob', 'admin', 'charlie', 'david']

# Loop through the list of usernames
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
