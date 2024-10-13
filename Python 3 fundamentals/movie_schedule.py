all_movies={"Black Panther":"11:00",
        "End Game":"01:00",
        "Thor":"03:00"}
print("Movies we are playing right now :")
for movie in all_movies:
    print(movie)
movie=input("Enter the movie you want to watch:\n")
time=all_movies.get(movie)
if time:
    print(movie,"is playing at",time)
else:
    print(movie,"is not playing")