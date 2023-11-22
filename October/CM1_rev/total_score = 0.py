total_score = 0

for i in range(4):
    score = int(input("Enter score for CM" + str(i+1) + ": "))
    percentage = (score / 100) * 100
    print("Percentage for CM" + str(i+1) + ": " + str(percentage) + "%")
    total_score += score

average_percentage = (total_score / 400) * 100
print("Average percentage for the year: " + str(average_percentage) + "%")
