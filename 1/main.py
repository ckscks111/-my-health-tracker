import pandas as pd
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sleep_hours = []
exercise_minutes = []
health_score = []
for day in days:
    print(f"\n---{day}---")
    sleep = float(input("How many hours did you sleep?"))
    exercise = int(input("How many minutes did you exercise?"))

    sleep_hours.append(sleep)
    exercise_minutes.append(exercise)
    score = 0
    if sleep >=7:
        score += 1
    if exercise >= 30:
        score += 1
    health_score.append(score)
data = {
    'Day' : days,
    'Sleep_Hours':sleep_hours,
    'Exercise_Minutes': exercise_minutes,
    'Health_Score': health_score
}

df=pd. DataFrame(data)
df.to_csv('health_data.csv', index=False)
print("\n✅ health_data.csv 저장 완료!")

def analyze_health(sleep_input, exercise_input) :
    if sleep_input <6 and exercise_input <10:
        return "You need serious rest and movement!"
    elif sleep_input <7 or exercise_input < 30:
        return "You're getting there. Small improvements can help!"
    else:
        return"Great job!"

print("\nDaily Health Analysis:\n")
for i in range(len(df)):
    day = df.loc[i,r'Day']
    sleep_val = df.loc[i,'Sleep_Hours']
    exercise_val = df.loc[i,'Exercise_Minutes']
    message = analyze_health(sleep_val,exercise_val)
    print(f"{day}:{message}")
