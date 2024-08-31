##Reading from a text file

filmFile = open("films.txt","r")
films = filmFile.read()
print(films)
filmFile.close()


filmFile = open("films.txt","r")
filmRec = filmFile.readline()

while filmRec != "":
    field = filmRec.split(",")
    ID = field[0]
    title = field[1]
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    if rating == "G":
        print(ID,title,rating,duration)  
        
    filmRec = filmFile.readline()
filmFile.close()


filmFile = open("films.txt","r")
filmRec = filmFile.readline()

while filmRec != "":
    field = filmRec.split(",")
    ID = field[0]
    title = field[1]
    rating = field[3]
    duration = int(field[4])
    genre = field[5]
    if genre == "Comedy\n":
        print(ID,title,rating,duration)
    filmRec = filmFile.readline()
filmFile.close()


