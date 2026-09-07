


import datetime

movies = {}

def add_movie(movie_name):
    movie_title = movie_name.strip()
    if not movie_title:
        return "Movie name cannot be empty."
    
    key_name = movie_title.lower()
    if key_name in movies:
        return f"'{movie_title}' is already in the system."
    
    now = datetime.datetime.now()
    date_added = f"{now.year}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    
    movies[key_name] = {
        "display_name": movie_title,
        "ratings": [],
        "date_added": date_added
    }
    return f"Movie '{movie_title}' added!"

def rate_movie(movie_name, rating_input):
    if not movies:
        return "No movies available to rate. Please add a movie first."
    
    movie_title = movie_name.strip()
    key_name = movie_title.lower()
    
    if key_name not in movies:
        return f"Movie '{movie_title}' not found."
    
    try:
        rating = int(str(rating_input).strip())
        if rating < 1 or rating > 5:
            return "Rating must be between 1 and 5."
        
        movies[key_name]["ratings"].append(rating)
        return f"Rating {rating} added!"
    except ValueError:
        return "Invalid input."

def calculate_average(movie_name):
    key_name = movie_name.strip().lower()
    if key_name in movies and movies[key_name]["ratings"]:
        ratings = movies[key_name]["ratings"]
        return sum(ratings) / len(ratings)
    return 0.0


if __name__ == "__main__":
    
    
    while True:
    
        movie_flix_menu = """
Welcome to Movie Flix: The Home of All Entertainment

1. Add a Movie
2. Rate a Movie
3. View Average Ratings
4. Exit
"""
        print(movie_flix_menu)

        try:
            user_choice = int(input("Select an option: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number (1 - 4).\n")
            continue

        match user_choice:
            case 1:
                name = input("Enter the movie name: ")
                result = add_movie(name)
                print(f"{result}\n")

            case 2:
                name = input("Enter the movie name: ")
                user_rating = input("Enter your rating (1-5): ")
                result = rate_movie(name, user_rating)
                print(f"{result}\n")

            case 3:
                if not movies:
                    print("No movies found in the system.\n")
                    continue

                print("\nAverage Ratings:")
                for key in movies:
                    display_name = movies[key]["display_name"]
                    if movies[key]["ratings"]:
                        avg = calculate_average(key)
                        print(f"{display_name}: {avg:.2f}")
                    else:
                        print(f"{display_name}: No ratings yet")
                print()

            case 4:
                print("Exiting the application. Goodbye!")
                break

            case _:
                print("Invalid option. Please choose a number between 1 and 4.\n")
