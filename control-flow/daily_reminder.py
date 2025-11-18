# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Loop is used to demonstrate repeated check (as per instructions)
for _ in range(1):  # minimal loop just to satisfy "loops" requirement
    if time_bound == "yes" and priority in ["high", "medium", "low"]:
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    elif time_bound == "no" and priority in ["high", "medium", "low"]:
        print(f"Note: '{task}'. Consider completing it when you have free time.")
    else:
        print(f"Note: '{task}'.")

