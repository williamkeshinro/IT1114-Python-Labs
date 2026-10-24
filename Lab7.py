# Step 1 prompt
staring_number = int(input("Enter a starting number: "))
ending_number = int(input("Enter an ending number: "))

# Step 2: Accept additional inputs
for number in range(staring_number, ending_number + 1):

# Step 3: Calculate 
    if_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            if_prime = False
            break
    
    if if_prime:
        print(f"{number}")
