task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: \'{task}\' is a high priority task that requires immediate attention today!")
        else:
            print("Note: \'{task}\' is a high priority task that requires immediate attention today!")    
    case "medium":
        if time_bound == "yes":
            print("Reminder: \'{task}\' is a medium priority. Consider completing it when you have free time.")
        else:
            print("Note: \'{task}\' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print("Reminder: \'{task}\' is a low priority. Consider completing it when you have free time.")
        else:
            print("Note: \'{task}\' is a low priority task. Consider completing it when you have free time.")