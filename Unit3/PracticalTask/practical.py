# Use float(input()) to collect two numbers from the user
num1 = float(input("Enter number one"))
num2 = float(input("Enter number two"))

# Calculate and display: addition, subtraction, multiplication, division
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# Calculate and display: floor division (//) and modulus (%)
print(num1 // num2)
print(num2 // num1)
print(num1 % 2)
print(num2 % 2)

# Round all results to 2 decimal places using round()
print(round(num1, 2))
print(round(num2, 2))

# Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
if num2 == 0:
    print("An error has occured please dont use 0")

# Display all results in a formatted table using f-strings
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")