# 1. Ask the user to input their secret password.
password = input("Enter your password: ")

# 2. Use .strip() to clean up any accidental spaces they might have typed at the start or end.
password = password.strip()

# 3. Grab the very first letter and the very last letter of the password using string indexing.
first = password[0]
last = password[-1]

# 4. Print a hint using an f-string that forces the letters into uppercase so they stand out. (e.g., “Your password hint: It starts with P and ends with N”).
print(f"Your password hint: It starts with {first} and ends with {last}")