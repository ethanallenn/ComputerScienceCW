from io import open

filmfile = open("films.txt", "r")
films = filmfile.readline()

while films != "":
    field = films.split(",")
    ID = field[0]
    title = field[1]
    year = int(field[2])
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    if year == "2016":
        print(ID, title, year, rating, duration, genre)

    films = filmfile.readline()
filmfile.close()