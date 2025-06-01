name = input("Your name: ")
sleep = float(input("How many hours did you sleep? ").strip())
exercise = int(input("How many minutes did you exercise? ").strip())
print("Hi", name + "!")
print("You slept", sleep, "hours and exercised", exercise, "minutes today.")
if int(exercise) >=30:
    print("Good job staying active today!")
else:
    print("Try to move a bit more tomorrow!")

if sleep >= 8:
    print("Well-rested!")
elif sleep >= 6:
    print("OK, but more sleep")
else:
    print("Try to sleep earlier tonight")

score=0
if sleep >= 8:
    score +=1
if int(exercise) >=30:
    score +=1

if score ==2:
    print("Good job!👍🏻")
elif score ==1:
    print("Not bad")
else:
    print("Let's focus on your health")

if sleep < 6 and int(exercise) < 10:
    print("Health Warning!!!!!")

days = ["Mon","Tue","Wed", "Thu","Fri"]
exercise_minutes = []
for day in days:
    mins = int(input(f"How may minutes did you exercise on {day}?"))
    exercise_minutes.append(mins)

print("\nYour weekly exercise summary:")
for i in range(len(days)):
    print(f"{days[i]}: {exercise_minutes[i]} min")

total=sum(exercise_minutes)
average=total/len(exercise_minutes)

print(f"\nTotal: {total} minutes")
print(f"Average: {round(average,1)} minutes")

if average >=30:
    print("Great job this week!👍🏻")
else:
    print("Try to be more. 🐢")
