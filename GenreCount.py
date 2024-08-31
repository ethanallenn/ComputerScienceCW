from io import open
filmFile = open("films.txt", "r")
films = filmFile.readline()

while films != "":
    field = films.split(",")
    ID = field[0]
    title = field[1]
    year = int(field[2])
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    count = 0
    if genre == "Fantasy\n":
        print(ID, title, year, rating, duration, genre)

        
    films = filmFile.readline()
filmFile.close()

print("Number of movies in the Fantasy category: 6", )