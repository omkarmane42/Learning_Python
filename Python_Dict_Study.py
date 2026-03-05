
# #HomeWork---->  Create Dictionary Of four Movies and their Cast.

# Dictionary of movies and actors
movies = {
    "Coolie": ["Rajnikant", "Nagarjuna Akkineni", "Shruti Haasan", "Amir Khan"],
    "Chhaava": ["Vicky Kaushal", "Rashmika Mandhana", "Akshay Khanna", "Ashutosh Rana"],
    "Dhurandar": ["Akshay Khanna", "Ranveer Singh", "Arjun Rampal", "Sanjay Datt"],
    "Housefull 5": ["Akshay Kumar", "Ritesh Deshmukh", "Abhishek Bachchan", "Sanjay Datt"]
}

# Print full dictionary
print("All Movies and Cast:")
print(movies)
print()

# Print movie names
print("Movie Names:")
for movie in movies.keys():   # Get All movies Names Using Keys()
    print(movie)
print()

# Print all cast names
print("All Cast Names:")
for cast_list in movies.values():   #Get All Cast Names Using Values()
    for actor in cast_list:
        print(actor)
print()

# Print movies with their cast
print("Movies and Their Cast:")
for movie, cast in movies.items():     #Using items() 
    print(movie, ":", cast)
print()

# Add a new movie
movies["Raid 2"] = ["Ajay Devgan", "Vaani Kapoor", "Tamannaah Bhatia", "Saurabh Shukla"]

print("After Adding New Movie:")
print(movies)
print()

# Count total movies
print("Total Number of Movies:", len(movies))
print()

# Count cast in each movie
print("Number of Cast in Each Movie:")
for movie, cast in movies.items():
    print(movie, ":", len(cast))
print()

# Search actor in movies
actor_name = "Akshay Khanna"

print("Searching Actor:", actor_name)
for movie, cast in movies.items():
    if actor_name in cast:
        print(actor_name, "is in", movie)