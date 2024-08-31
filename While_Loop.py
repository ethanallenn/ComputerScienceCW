while True:
    result = input("Enter your result (or 'q' to quit): ")
    if result == 'q':
        break
    try:
        result = int(result)
        if result >= 90:
            print("Your mark is A+")
        elif result >= 80:
            print("Your mark is A")
        elif result >= 70:
            print("Your mark is B")
        elif result >= 60:
            print("Your mark is C")
        elif result >= 50:
            print("Your mark is D")
        else:
            print("Your mark is F")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
