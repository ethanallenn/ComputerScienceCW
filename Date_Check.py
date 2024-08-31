import re

date = input("Enter today's date: ")
def rangeCheck(date):
    if re.match("[0-9]{2}/[0-9]{2}/[0-9]{4}", date):
        return True
    else:
        return False
    
print(rangeCheck(date))