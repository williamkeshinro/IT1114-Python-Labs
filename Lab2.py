
# Prompt user for the time spent in the parking lot in minutes
minutes = float(input("Enter the number of minutes parked: "))

# Determine rate per hour based on time spent
if minutes < 30:
    rate = 0.0
elif minutes <= 60:
    rate = 1.00
elif minutes <= 180:  # 1 to 3 hours (180 minutes)
    rate = 1.25
elif minutes <= 300:  # 3 to 5 hours (300 minutes)
    rate = 1.50
else:                 # More than 5 hours (300 minutes)
    rate = 2.00

# Calculate total parking cost using the provided formula
cost = rate * (minutes / 60)

# Display the result
print(f"Total parking cost: {cost}")