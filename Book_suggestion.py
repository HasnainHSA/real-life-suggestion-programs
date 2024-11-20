print("Welcome to Book Recommendation Program!")
genre = input("Enter your preferred book genre (Fiction/Non-fiction/Mystery): ").lower()
length = input("Do you prefer short or long books? (Short/Long): ").lower()

book = ""
while book == "":
    if genre == "fiction" and length == "short":
        book = "The Alchemist by Paulo Coelho"
    elif genre == "non-fiction" and length == "long":
        book = "Sapiens by Yuval Noah Harari"
    elif genre == "mystery" and length == "short":
        book = "The Hound of the Baskervilles by Arthur Conan Doyle"
    else:
        print("No suitable books found. Try again!")
        genre = input("Enter your preferred book genre (Fiction/Non-fiction/Mystery): ").lower()
        length = input("Do you prefer short or long books? (Short/Long): ").lower()

print(f"Suggested Book: {book}")
