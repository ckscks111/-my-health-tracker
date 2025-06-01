import pandas as pd

df=pd.read_csv('../health_data.csv')
print("\n🚪Loaded CSV data:")
print(df)

def analyze_health_data(csv_file='health_data.csv'):
    data_df = pd.read_csv(csv_file)
    print("\n🚪Loaded CSV data:")
    print(data_df)

sleep_avg = df['Sleep_Hours'].mean()
exercise_avg = df['Exercise_Minutes'].mean()

print(f"\n🎯 Average Sleep Hours: {round(sleep_avg,1)}")
print(f"🎯 Average Exercise Minutes: {round(exercise_avg,1)}")

df['Health_Score'] = 0
df.loc[df['Sleep_Hours']>=7, 'Health_Score']+=1
df.loc[df['Exercise_Minutes']>=30, 'Health_Score']+=1

print(df[['Day', 'Health_Score']])

df_sorted = df.sort_values(by='Health_Score',ascending=False)
print("\n👍🏻 TOP 3 Healthy Days:")
print(df_sorted[['Day', 'Health_Score']].head(3))

warning_days = df[(df['Sleep_Hours']<6 &(df['Exercise_Minutes']<15))]
print("\n🐢Health Warning Days(Sleep<6 and Exercise <15):")
print(warning_days[['Day', "Sleep_Hours","Exercise_Minutes"]])
