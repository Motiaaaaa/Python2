num_of_guests = int(input("Number of Guests: "))

NUM_PEOPLE_LG_PIZZA = 7
NUM_PEOPLE_MED_PIZZA = 3
NUM_PEOPLE_SM_PIZZA = 1

large_pizzas = num_of_guests // NUM_PEOPLE_LG_PIZZA
remaining_guests = num_of_guests % NUM_PEOPLE_LG_PIZZA

medium_pizzas = remaining_guests // NUM_PEOPLE_MED_PIZZA
remaining_guests = remaining_guests % NUM_PEOPLE_MED_PIZZA

small_pizzas = remaining_guests // NUM_PEOPLE_SM_PIZZA


print("You will need " + str(large_pizzas) + " large pizzas, " + str(medium_pizzas) + " medium pizzas, and " + str(small_pizzas) + " small pizzas.")

