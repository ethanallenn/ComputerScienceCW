password = "213343"
while password!="000":
    password=input("Enter password: ")
    if password=="213343":
        print("Password accepted")
    else:
        print("Password incorrect")
        forget = ("Do you forget your password?")
        if forget == "yes":
            print("Exiting loop:")
            break