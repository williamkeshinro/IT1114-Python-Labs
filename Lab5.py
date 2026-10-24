
# Step 1 Ask the user for monthly sales goal
sales_goal = float(input("What is your monthly sales goal?: "))
employee_count = 0
sales_total = 0
another_person = "y"
# Step 2 Ask the user for sales amounts until they indicate they are done
while another_person == "y":
    employee_count = employee_count + 1
    person_total = 0

    for week in range(4):
        weekly_sales = float(input("Enter sales for week: "))
        person_total = person_total + weekly_sales

    sales_total = sales_total + person_total
    another_person = input("Is there another employee to enter sales for? (y/n): ")
#Step 4 Managers bounus
if sales_total > sales_goal:
    manager_bonus = sales_total * 0.05
else:
    manager_bonus = sales_total * 0.02
#Step 4 Display the outputs
print(f"Number of Employees: {employee_count}")
print(f"Department Sales Goal: {sales_goal}")
print(f"Total sales: {sales_total}")
print(f"Manager Bonus: {manager_bonus}")
