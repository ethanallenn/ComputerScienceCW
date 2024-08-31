soldTickets = int(input("Enter number of tickets sold: "))
def rangeCheck(soldTickets):
    if soldTickets <0 or soldTickets >=120:
        return "This information is invalid. Please re-enter amount of tickets sold."
    else:
        return("Number of tickets sold is: ", soldTickets)
    
soldTickets = int(input("Enter amount of tickets sold: "))
print(rangeCheck(soldTickets))
