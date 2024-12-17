#pip install matplotlib sqlite3

import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Initialize the database connection
conn = sqlite3.connect('habits.db')
c = conn.cursor()

# Create a table to store habits
c.execute('''
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_name TEXT NOT NULL,
        log_date TEXT NOT NULL
    )
''')
conn.commit()

# Function to log a habit
def log_habit(habit_name):
    log_date = datetime.now().strftime('%Y-%m-%d')
    c.execute('INSERT INTO habits (habit_name, log_date) VALUES (?, ?)', (habit_name, log_date))
    conn.commit()
    print(f"Habit '{habit_name}' logged for {log_date}")

# Function to check current streak of a habit
def check_streak(habit_name):
    c.execute('SELECT log_date FROM habits WHERE habit_name = ? ORDER BY log_date DESC', (habit_name,))
    logs = c.fetchall()
    
    if not logs:
        return 0

    streak = 0
    last_date = datetime.strptime(logs[0][0], '%Y-%m-%d')

    # Go through log dates and count consecutive days
    for log in logs:
        current_date = datetime.strptime(log[0], '%Y-%m-%d')
        if last_date - current_date <= timedelta(days=1):
            streak += 1
        else:
            break
        last_date = current_date
    
    return streak

# Function to display habit progress over time
def visualize_habit(habit_name):
    c.execute('SELECT log_date FROM habits WHERE habit_name = ? ORDER BY log_date', (habit_name,))
    logs = c.fetchall()
    
    if not logs:
        print(f"No logs found for habit '{habit_name}'")
        return
    
    dates = [datetime.strptime(log[0], '%Y-%m-%d') for log in logs]
    streak_counts = list(range(1, len(dates) + 1))

    # Plot habit progress over time
    plt.figure(figsize=(10, 6))
    plt.plot(dates, streak_counts, marker='o', linestyle='-', color='b')
    plt.title(f"Progress of Habit '{habit_name}'")
    plt.xlabel('Date')
    plt.ylabel('Streak Count')
    plt.grid(True)
    plt.show()

# Function to list all logged habits
def list_habits():
    c.execute('SELECT DISTINCT habit_name FROM habits')
    habits = c.fetchall()
    if not habits:
        print("No habits found.")
    else:
        print("Tracked Habits:")
        for habit in habits:
            print(f"- {habit[0]}")

# Example usage
while True:
    print("\n--- Habit Tracker Menu ---")
    print("1. Log a habit")
    print("2. Check streak")
    print("3. Visualize habit progress")
    print("4. List habits")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        habit_name = input("Enter habit name: ")
        log_habit(habit_name)
    
    elif choice == '2':
        habit_name = input("Enter habit name: ")
        streak = check_streak(habit_name)
        print(f"Current streak for '{habit_name}' is {streak} days.")
    
    elif choice == '3':
        habit_name = input("Enter habit name: ")
        visualize_habit(habit_name)
    
    elif choice == '4':
        list_habits()
    
    elif choice == '5':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Try again.")
