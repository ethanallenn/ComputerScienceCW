name = input("ENTER YOUR NAME: ")

def prescenceCheck(info):
    if name == "":
        return False
    else:
        return True
    
print(prescenceCheck(name))