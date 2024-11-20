print("Welcome to Travel Destination Suggestion!")
budget = int(input("Enter your budget in USD: "))
season = input("Enter your preferred season (Summer/Winter): ").lower()

destination = ""
while destination == "":
    if budget >= 2000 and season == "summer":
        destination = "Maldives"
    elif budget >= 1500 and season == "winter":
        destination = "Switzerland"
    elif budget < 1500 and season == "summer":
        destination = "Thailand"
    elif budget < 1500 and season == "winter":
        destination = "Iceland"
    else:
        print("No suitable destinations found. Try again!")
        budget = int(input("Enter your budget in USD: "))
        season = input("Enter your preferred season (Summer/Winter): ").lower()

print(f"Suggested Destination: {destination}")
