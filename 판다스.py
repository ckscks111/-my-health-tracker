import pandas as pd

data={
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sleep_Hours' : [6.5,7,5.5,8,4],
    'Exercise_Minutes': [25,40,15,35,10]
}

df = pd.DataFrame(data)
#df.to_csv('health_log.csv', index=False)
#print("CSV 저장 완료!")

#df = pd.read_csv('health_log.csv')
#print("평균 수면 시간:", round(df['Sleep_Hours'].mean(),1),"hours")
#print("평균 운동 시간:", round(df['Exercise_Minutes'].mean(),1),"minutes")

#print("\n[수면 부족한 날]")
#print(df[df['Sleep_Hours']<6])
#print("\n[운동 잘한 날]")
#print(df[df['Exercise_Minutes']>=30])

#print("\n[평소보다 운동 많이한 날]")
#print(df[df['Exercise_Minutes']>df['Exercise_Minutes'].mean()])

exercise_avg = df['Exercise_Minutes'].mean()
sleep_avg = df['Sleep_Hours'].mean()

more_exercise = df[df['Exercise_Minutes'] > exercise_avg]
print(more_exercise)
print("You exercised more than average on", len(more_exercise), "days.")

less_sleep = df[df['Sleep_Hours']<sleep_avg]
print(less_sleep)
print("You slept less than average on", len(less_sleep), "days.")

healthy_days = df[(df['Exercise_Minutes'] > exercise_avg) & (df['Sleep_Hours'] > sleep_avg)]
print(healthy_days)