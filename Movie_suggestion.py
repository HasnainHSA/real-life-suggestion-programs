print("Welcome to Movie Suggestion Program!")
genre = input("Enter your preferred genre (Action/Comedy/Drama):").lower()
rating = int(input("Enter the minimum IMDb rating (1-10): "))

movie = ""
while movie == "":
    if genre == "action" and rating >= 8:
        movie = "Mad Max: Fury Road"
    elif genre == "comedy" and rating >= 7:
        movie = "The Grand Budapest Hotel"
    elif genre == "drama" and rating >= 8:
        movie = "The Shawshank Redemption"
    else:
        print("No suitable movies found. Try again!")
        genre = input("Enter your preferred genre (Action/Comedy/Drama): ").lower()
        rating = int(input("Enter the minimum IMDb rating (1-10): "))

print(f"Suggested Movie: {movie}")
