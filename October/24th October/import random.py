import random
scores = [["AAA01", 135], ["BBBOI", 87], ["CCCOI", 188], ["DDDOI", 109]]
user_id = input("Enter your ID: ")

found = False
for i in range(len(scores)):
    if scores[i][0] == user_id:
        found = True
        break
if not found:
    scores.append([user_id, 0])
new_score = random.randint(50, 200)
for i in range(len(scores)):
    if scores[i][0] == user_id:
        if new_score > scores[i][1]:
            scores[i][1] = new_score
        break
print("User ID\tTop Score")
for i in range(len(scores)):
    print(scores[i][0] + "\t" + str(scores[i][1]))
