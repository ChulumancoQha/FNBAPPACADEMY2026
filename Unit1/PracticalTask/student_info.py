# Let us collect info - Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float)
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favNumber = float(input("Enter your favourite number: "))

# Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’
print(f"Welcome, {name} {surname}")

# Display the name in UPPERCASE using .upper() and in Title Case using .title()
print(name.upper())
print(name.title())

# Calculate and display the age in months (age × 12)
month = age * 12
print(f"You are {month} months old.")

# Round the favourite number to 2 decimal places using round()
print(round(favNumber, 2))

# Print the data type of each collected value using type()
print(type(name))
print(type(surname))
print(type(age))
print(type(favNumber))