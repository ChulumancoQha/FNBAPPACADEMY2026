# Collect first name, last name, and bio message using input()
name = input("Enter your name: ")
surname = input("Enter your surname: ")
bio = input("Enter your bio message: ")

# Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
username = f"{name[0]}{surname}".lower()

# Display the full name in Title Case using .title()
print(f"{name.title()} {surname.title()}")

# Strip leading/trailing whitespace from the bio before displaying it using .strip()
bio = bio.strip()
print(bio)

# Count and display the number of characters in the bio using len()
print(len(bio))

# Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
bio = bio.replace("I am", "I'm")

# Display all output using f-strings
print(f"Hi, {name} {surname}, this is your bio: {bio}")