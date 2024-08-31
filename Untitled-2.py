name = input("Enter student name: ")
marks = []
for i in range(10):
    marks.append(float(input(f"Enter marks for test {i+1}: ")))
average = sum(marks) / len(marks)
sorted_marks = sorted(marks, reverse=True)
print(f"Student Name: {name}")
print(f"Average Mark: {average}")
print(f"Top Three Marks: {sorted_marks[:3]}")
print(f"Bottom Three Marks: {sorted_marks[-3:]}")
