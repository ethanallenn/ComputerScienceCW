names = []
while True:
    name = input("Enter a name or 'End' to stop: ")
    if name == "End":
        break
    names.append(name)
half_index = len(names) // 2
if len(names) % 2 == 0:
    first_half = names[:half_index]
else:
    first_half = names[:half_index + 1]
print(first_half)