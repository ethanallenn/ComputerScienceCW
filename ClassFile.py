class_file = open('class.txt', 'w')

while True:
    first_name = input("Enter first name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    town = input("Enter town: ")
    record = f"{first_name},{surname},{age},{gender},{town}\n"
    class_file.write(record)
    add_another = input("Do you want to add another record? (yes/no): ")
    if add_another.lower() != "yes":
        break

class_file.close()