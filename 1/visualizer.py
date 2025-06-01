import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Arial'

df= pd.read_csv('../health_data.csv')
days= df['Day']
sleep = df['Sleep_Hours']
exercise = df['Exercise_Minutes']

plt.figure(figsize=(10,5))
plt.plot(days, sleep, marker='o', label='Sleep_Hours')
plt.plot(days, exercise, marker='s', label='Exercise Minutes')
plt.title('Weekly Sleep and Exercise Tracker')
plt.xlabel('Day')
plt.ylabel('Hours/Minutes')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,4))
plt.bar(df['Day'],df['Health_Score'], color='skyblue')
plt.title('Health Score by Day')
plt.xlabel('Day')
plt.ylabel('Health Score')
plt.ylim(0,2)
plt.tight_layout()
plt.show()