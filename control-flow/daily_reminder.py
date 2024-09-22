

def main():
    
    task = input("Enter your task: ")

    
    priority = input("Priority (high/medium/low): ").lower()
    while priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Priority (high/medium/low): ").lower()

    
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    while time_bound not in ["yes", "no"]:
        print("Invalid response. Please enter 'yes' or 'no'.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

    
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."
    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."
    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
