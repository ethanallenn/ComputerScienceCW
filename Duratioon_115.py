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
    if duration > 115:
        print(title, durationn)

    films = filmFile.readline()
filmFile.close()