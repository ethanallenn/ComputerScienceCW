import re

def length_check(code):
    if not re.match("^[B][T]\d{2} \d[A-Z]{2}$", code):
        print("Invalid postcode format!")
        return "INVALID POSTCODE"
    else:
        return "VALID POSTCODE " + code
    
var = input("Enter your post code: ")
print(length_check(var))

if var != "INVALID POSTCODE":
    print("This Postcode must meet the criteria!")