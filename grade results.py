cs_value = input("Did you pass GCSE Computer Science? Y/N ")
fm_value = input("Did you pass GCSE Further Maths? Y/N ")
if cs_value == "Y" + fm_value == "N":
    print("You should take this subject!")
else:
    print("You should take Digital Technology instead!")