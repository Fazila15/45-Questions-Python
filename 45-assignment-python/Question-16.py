# Original guest list
guest_list = ["Mashal Afzal", "Mubashir Ali", "Hamza Aftab"]

# Informing that a bigger table is available
print("Great news! I found a bigger dinner table, so I'm inviting more guests.\n")

# Adding new guests
guest_list.insert(0, "Amjad Ali")  # Adding at the beginning
guest_list.insert(2, "Naeem Hussain")  # Adding in the middle
guest_list.append("Areeba")  # Adding at the end

# Printing the new set of invitations
print("Updated Invitation Messages:")
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you for dinner.")
