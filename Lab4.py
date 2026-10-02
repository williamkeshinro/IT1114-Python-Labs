
# Step 1: Accept user inputs
balance = float(input("Enter beginning balance: "))
monthly_rate_percent = float(input("Enter monthly interest rate (%): "))
months = int(input("Enter number of months: "))

# Convert percentage to decimal
monthly_rate = monthly_rate_percent / 100.0

# Step 2: Print table headers
print("\nMonth\tInterest\tBalance")

# Step 3: Loop through each month to calculate interest and updated balance
for month in range(1, months + 1):
    interest_paid = balance * monthly_rate
    balance += interest_paid
    print(f"{month}\t{interest_paid:.2f}\t\t{balance:.2f}")