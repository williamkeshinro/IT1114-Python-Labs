
# Step 1: Prompt the user for room dimensions and flooring cost
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
cost_per_sqft = float(input("Enter cost per sq. foot: "))

# Step 2: Calculate square footage and flooring cost
square_feet = length * width
flooring_cost = square_feet * cost_per_sqft

# Step 3: Calculate 7% tax and the final total amount due
tax = flooring_cost * 0.07
total_due = flooring_cost + tax

# Step 4: Display the outputs
print()
print(f"Square feet: {square_feet}")
print(f"Flooring: {flooring_cost}")
print(f"Tax: {tax}")
print(f"Total: {total_due}")