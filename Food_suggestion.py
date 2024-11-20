print("Welcome to Food Suggestion Program!")
cuisine = input("Enter your preferred cuisine (Italian/Chinese/Pakistani): ").lower()
spice_level = input("Do you prefer spicy food? (Yes/No): ").lower()

dish = ""
while dish == "":
    if cuisine == "italian" and spice_level == "no":
        dish = "Margherita Pizza"
    elif cuisine == "chinese" and spice_level == "yes":
        dish = "Kung Pao Chicken"
    elif cuisine == "pakistani" and spice_level == "yes":
        dish = "Biryani"
    elif cuisine == "pakistani" and spice_level == "no":
        dish = "nihari"
    else:
        print("No suitable dishes found. Try again!")
        cuisine = input("Enter your preferred cuisine (Italian/Chinese/Indian): ").lower()
        spice_level = input("Do you prefer spicy food? (Yes/No): ").lower()

print(f"Suggested Dish: {dish}")
