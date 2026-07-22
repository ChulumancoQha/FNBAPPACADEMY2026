# Ask the user how many kilometers they want to drive.
kilometers = float(input("Please enter the amout of kilometers you want to drive: "))

# 2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).
petrol_price = float(input("Enter the current petrol price per liter: R"))
petrol_price = round(petrol_price, 2)

# 3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
liters_needed = round(kilometers / 10, 2)

# 4. Calculate the total cost (liters_needed * petrol_price).
total_cost = round(liters_needed * petrol_price, 2)

# 5. Use type casting to ensure your numbers work, and use round() to format the
# final cost to 2 decimal places.

print(total_cost)
