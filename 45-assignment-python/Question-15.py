# Original guest list
guest_list = ["Mashal Afzal", "Mubashir Ali", "Hamza Aftab"]

# Guest who can't make it
unavailable_guest = guest_list[0]
print(f"Unfortunately, {unavailable_guest} can't make it to dinner.")

# Replacing the unavailable guest with a new guest
guest_list[0] = "Amjad Ali"

# Printing new invitation messages
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you for dinner.")
