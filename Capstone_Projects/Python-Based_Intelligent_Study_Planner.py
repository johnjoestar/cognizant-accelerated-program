from datetime import datetime

# Phase 1: Task Management  
# Develop input methods for tasks and schedules.
tasks = []

def add_task():
    name = input("Enter task name: ")
    deadline = input("Enter deadline (DD-MM-YYYY): ")
    priority = int(input("Enter priority (1 = Low, 2 = Medium, 3 = High): "))
    try:
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y")
        tasks.append({
            "name": name,
            "deadline": deadline_date,
            "priority": priority
        })
        print(f"Task '{name}' added successfully.")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")

def show_schedule():
    print("\nPrioritized Task Schedule:")
    sorted_tasks = sorted(tasks, key=lambda x: (x['deadline'], x['priority']))
    for task in sorted_tasks:
        print(f"- {task['name']} | Due: {task['deadline'].date()} | Priority: {task['priority']}")

# Phase 2: Performance Tracking  
# Implement score tracking and weak area identification.
scores = {}

def add_score():
    subject = input("Enter subject name: ").capitalize()
    try:
        score = float(input("Enter score (0-100): "))
        if subject not in scores:
            scores[subject] = []
        scores[subject].append(score)
        print(f"Score added for {subject}.")
    except ValueError:
        print("Please enter a valid numeric score.")

def show_performance():
    print("\nPerformance Summary:")
    for subject, subject_scores in scores.items():
        avg = sum(subject_scores) / len(subject_scores)
        feedback = "Failing" if avg < 70 else "Passing"
        print(f"- {subject}: Avg = {avg:.2f} -> {feedback}")

# Phase 3: Error Handling  
# Manage invalid inputs and enhance application stability. 
def main():
    while True:
        print("\nStudent Assistant Menu")
        print("1. Add Task")
        print("2. Show Task Schedule")
        print("3. Add Score")
        print("4. Show Performance Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        try:
            if choice == '1':
                add_task()
            elif choice == '2':
                show_schedule()
            elif choice == '3':
                add_score()
            elif choice == '4':
                show_performance()
            elif choice == '5':
                print("Exiting. Keep up the good work!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

main()
