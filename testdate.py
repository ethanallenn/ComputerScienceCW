import re
date = input("Input today's date: ")
def formatcheck(date):
    if re.match("[A-Z]{2}/[0-9]{2}/23", date):
        return True
    else:
        return False

print(formatcheck(date))