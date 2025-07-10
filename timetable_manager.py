timetable = {}

def add_class(day, period, subject):
    if day not in timetable:
        timetable[day] = {}
    if period in timetable[day]:
        print("Conflict! There's already a class scheduled at this time.")
    else:
        timetable[day][period] = subject
        print(f"Added: {subject} on {day} during {period}")

def view_timetable():
    if not timetable:
        print("No classes scheduled yet.")
        return
    print("\n----- Timetable -----")
    for day, periods in timetable.items():
        print(f"{day}:")
        for period, subject in periods.items():
            print(f"  {period} - {subject}")
    print("---------------------\n")

def main():
    while True:
        print("\nTimetable Management System")
        print("1. Add Class")
        print("2. View Timetable")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            day = input("Enter day (e.g., Monday): ")
            period = input("Enter period (e.g., 9AM-10AM): ")
            subject = input("Enter subject name: ")
            add_class(day, period, subject)
        elif choice == '2':
            view_timetable()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
