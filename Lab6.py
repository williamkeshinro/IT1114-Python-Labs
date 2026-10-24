
# Step 1: Accept initial inputs

# Room_Types: 
Room_1 = 375 
Room_2 = 350 
Room_3 = 525 
Room_4 = 475 

# Meal_Types:
Brunch = 25 
Dinner = 75 

# Excursion_Types:
Picnic = 50 
Snorkeling = 25
Guided_Hike = 17
Boat_Dinner = 200

# Step 2: Accept additional inputs

Number_of_nights = int(input("How many nights did you stay?: "))
Type_of_room = input("What type of room did you stay in? (1, 2, 3, or 4): ")
Number_of_brunches = int(input("How many brunches did you have?: "))
Number_of_dinners = int(input("How many dinners did you have?: "))
Picnic_Choice = input("Did you have the Picnic excursion? (y/n): ") .lower() == "y"
Snorkeling_Choice = input("Did you have the Snorkeling excursion? (y/n): ") .lower() == "y"
Guided_Hike_Choice = input("Did you have the Guided Hike excursion? (y/n): ") .lower() == "y"
Boat_Dinner_Choice = input("Did you have the Boat Dinner excursion? (y/n): ") .lower() == "y"

# Step 3: Calculate costs

def roomCost(Type_of_room, Number_of_nights):
    if Type_of_room == "1":
        room_cost = Room_1
    elif Type_of_room == "2":
        room_cost = Room_2
    elif Type_of_room == "3":
        room_cost = Room_3
    elif Type_of_room == "4":
        room_cost = Room_4
    else:
        room_cost = 0

    total_room_cost = room_cost * Number_of_nights
    return total_room_cost

def mealCost(Number_of_brunches, Number_of_dinners):
    total_meal_cost = (Number_of_brunches * Brunch) + (Number_of_dinners * Dinner)
    gratuity =  total_meal_cost * 0.15
    total_meal_cost = total_meal_cost + gratuity
    return total_meal_cost

def excursionCost(Picnic_Choice, Snorkeling_Choice, Guided_Hike_Choice, Boat_Dinner_Choice):
    total_excursion_cost = 0

    if Picnic_Choice:
        total_excursion_cost += Picnic

    if Snorkeling_Choice:
        total_excursion_cost += Snorkeling

    if Guided_Hike_Choice:
        total_excursion_cost += Guided_Hike

    if Boat_Dinner_Choice:
        total_excursion_cost += Boat_Dinner

    return total_excursion_cost

# Step 4: Display outputs
print(f"Room Cost: ${roomCost(Type_of_room, Number_of_nights):.2f}")
print(f"Meal Cost: ${mealCost(Number_of_brunches, Number_of_dinners):.2f}")
print(f"Excursion Cost: ${excursionCost(Picnic_Choice, Snorkeling_Choice, Guided_Hike_Choice, Boat_Dinner_Choice):.2f}")
print(f"Total Cost: ${roomCost(Type_of_room, Number_of_nights) + mealCost(Number_of_brunches, Number_of_dinners) + excursionCost(Picnic_Choice, Snorkeling_Choice, Guided_Hike_Choice, Boat_Dinner_Choice):.2f}")
