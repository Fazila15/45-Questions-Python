# List of places I'd like to visit (not in alphabetical order)
places = ["Japan", "Iceland", "Switzerland", "New Zealand", "Norway"]

# Printing the original list
print("Original order:")
print(places)

# Printing the list in alphabetical order without modifying the original list
print("\nAlphabetical order:")
print(sorted(places))

# Showing that the list is still in its original order
print("\nStill in original order:")
print(places)

# Printing the list in reverse alphabetical order without modifying the original list
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# Showing that the list is still in its original order
print("\nStill in original order:")
print(places)

# Reversing the order of the list and printing it
places.reverse()
print("\nReversed order:")
print(places)

# Reversing the order again to get back to the original order
places.reverse()
print("\nBack to original order:")
print(places)

# Sorting the list in alphabetical order and modifying the actual list
places.sort()
print("\nSorted in alphabetical order:")
print(places)

# Sorting the list in reverse alphabetical order and modifying the actual list
places.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places)
