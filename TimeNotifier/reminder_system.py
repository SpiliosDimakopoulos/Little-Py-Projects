#pip install schedule plyer
import schedule
import time
from plyer import notification

# Function to send a notification
def send_reminder(reminder_text):
    notification.notify(
        title="Reminder",
        message=reminder_text,
        timeout=10  # Duration the notification stays on screen (seconds)
    )

# Function to schedule a reminder
def set_reminder(reminder_text, schedule_time):
    print(f"Reminder set: {reminder_text} at {schedule_time}")
    schedule.every().day.at(schedule_time).do(send_reminder, reminder_text=reminder_text)

# Example usage: setting multiple reminders
set_reminder("Meeting with the team", "14:30")
set_reminder("Take a break", "16:00")

# Run the scheduled reminders
while True:
    schedule.run_pending()
    time.sleep(1)
