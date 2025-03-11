# Question 2

# Ask the user to enter their first name and then ask them to enter their surname. Join them together with a
# space between and display the name and the length of whole name.

# Ask the user to enter their first name
first_name = input("Enter your first name: ")

# Ask the user to enter their surname
surname = input("Enter your surname: ")

# Join the first name and surname with a space
full_name = first_name + " " + surname

# Calculate and display the length of the full name
name_length = len(full_name)

print(f"Your full name is: {full_name}")
print(f"The length of your full name (including space) is: {name_length} characters.")
