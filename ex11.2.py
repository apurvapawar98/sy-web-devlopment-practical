days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9 AM", "10 AM", "11 AM", "12 PM", "1 PM"]

schedule = [["Free" for _ in days] for _ in hours]


def display_schedule():
    print("\nDaily Class Schedule")
    print("-" * 70)

    print(f"{'Time':<10}", end="")
    for day in days:
        print(f"{day:<12}", end="")
    print()

    for i, hour in enumerate(hours):
        print(f"{hour:<10}", end="")
        for j in range(len(days)):
            print(f"{schedule[i][j]:<12}", end="")
        print()


while True:
    display_schedule()

    print("\n1. View subject")
    print("2. Overwrite subject")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        day = input("Enter day: ").capitalize()
        hour = input("Enter hour (e.g. 10 AM): ").upper()

        if day in days and hour in [h.upper() for h in hours]:
            row = [h.upper() for h in hours].index(hour)
            column = days.index(day)
            print(f"Subject: {schedule[row][column]}")
        else:
            print("Invalid day or hour.")

    elif choice == "2":
        day = input("Enter day: ").capitalize()
        hour = input("Enter hour (e.g. 10 AM): ").upper()
        subject = input("Enter new subject/topic: ")

        if day in days and hour in [h.upper() for h in hours]:
            row = [h.upper() for h in hours].index(hour)
            column = days.index(day)

            schedule[row][column] = subject
            print("Schedule updated successfully!")
        else:
            print("Invalid day or hour.")

    elif choice == "3":
        print("Exiting schedule manager.")
        break

    else:
        print("Invalid choice.")
