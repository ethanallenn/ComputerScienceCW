def rangeCheck(age):
    if age >=18 or age <=0:
        return "NOT PERMITTED"
    else:
        return "PERMITTED" 

age = int(input("Enter your age: "))
print(rangeCheck(age))