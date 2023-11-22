def prescenceCheck(info):
    if info == "":
        return False
    else:
       return True

name = input("ENTER YOUR NAME: ")
print(prescenceCheck(name))