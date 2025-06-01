# 🩺 My Weekly Health Tracker

A simple Python-based project to help you log, analyze, and visualize your weekly sleep and exercise habits.

## 📁 Project Structure

.
├── main.py               # Collects user input and stores health data
├── analysis.py           # Analyzes health data and prints insights
├── visualizer.py         # Creates graphs for weekly health trends
├── health_data.csv       # Saved user data (generated)
├── README.md             # Project overview

## 🚀 How It Works


```bash
Step 1: Run the Tracker
python main.py

	•	You’ll be asked to input your sleep hours and exercise minutes for Monday to Friday.
	•	A CSV file health_data.csv will be saved.

Step 2: Analyze Your Health

python analysis.py

	•	Calculates average sleep and exercise.
	•	Highlights the top 3 healthy days.
	•	Gives a warning if your sleep or activity was too low.

Step 3: Visualize Trends

python visualizer.py

	•	Line graph: Sleep & exercise trends over the week.
	•	Bar chart: Daily health scores (0–2).

🧠 Logic Behind Health Score
	•	+1 if sleep >= 7 hours
	•	+1 if exercise >= 30 minutes
	•	Total possible per day: 2 points

📦 Requirements
	•	Python 3.x
	•	pandas
	•	matplotlib

Install with:
pip install pandas matplotlib

💡 Future Ideas
	•	Weekly goal setting and progress tracking
	•	Optional weekend logging
	•	Integration with health APIs (e.g., Apple Health)