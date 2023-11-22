firstname = input("Enter your firstname: ")
surname = input("Enter your surname: ")
number = input("Enter a 4 digit number: ")
username = number[0] + firstname[0] + number[1:3] + surname[0] + number[3]
print("Your username is:", username)