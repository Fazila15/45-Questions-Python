# Original guest list
guest_list = ['Amjad Ali', 'Mashal Afzal', 'Naeem Hussain', 'Mubashir Ali', 'Hamza Aftab', 'Areeba']

# Informing that only two guests can be invited
print("Unfortunately, the new dinner table won’t arrive in time, so I can invite only two people for dinner.\n")

# Removing guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Informing the remaining two guests that they are still invited
print("\nUpdated Invitation Messages:")
for guest in guest_list:
    print(f"Dear {guest}, you are still invited to dinner.")

# Removing the last two guests
guest_list.pop()
guest_list.pop()

# Printing the empty guest list
print("\nFinal guest list:", guest_list)
