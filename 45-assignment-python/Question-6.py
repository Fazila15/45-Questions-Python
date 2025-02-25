# Storing the person's name with whitespace characters (\t and \n)
name = "\t\n  Albert Einstein  \n\t"

# Printing the name with the whitespace characters visible using repr()
print("Name with whitespace:", repr(name))

# Stripping the whitespace and printing the clean name
clean_name = name.strip()
print("Name after stripping whitespace:", repr(clean_name))
