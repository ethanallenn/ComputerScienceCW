import re
code = input("Enter your post code: ")
def length_check(code):
    if ("[BT][0-9]{3}[A-Z]{2}", ):
        print("Postcode must be 8 digits long!")
        return False
    else:
        return True
    
print(length_check())