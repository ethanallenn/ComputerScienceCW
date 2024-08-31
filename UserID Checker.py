import re

UserID = input("Enter your User ID: ")
ValidID = re.match("[A-Z][1-7][0-9]{3}", UserID)
if ValidID:
    print("Your UserID is Valid!")
else:
    print("Your ID is invalid. Please try again.")