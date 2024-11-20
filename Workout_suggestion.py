print("Welcome to Workout Suggestion Program!")
goal = input("What is your fitness goal? (Weight Loss/Muscle Gain/Flexibility): ").lower()
time = int(input("How many minutes can you dedicate daily? "))

workout = ""
while workout == "":
    if goal == "weight loss" and time >= 30:
        workout = "Cardio Exercises (Running, Cycling)"
    elif goal == "muscle gain" and time >= 45:
        workout = "Strength Training (Weight Lifting)"
    elif goal == "flexibility" and time >= 15:
        workout = "Yoga or Stretching Exercises"
    else:
        print("No suitable workouts found. Try again!")
        goal = input("What is your fitness goal? (Weight Loss/Muscle Gain/Flexibility): ").lower()
        time = int(input("How many minutes can you dedicate daily? "))

print(f"Suggested Workout: {workout}")
