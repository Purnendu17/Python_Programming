from tokenize import Double


class Activity:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def is_valid(self):
        """Check if the activity time is between 6 AM and 10 AM."""
        if 6 <= self.start_time <= 10 and 6 <= self.end_time <= 10 and self.start_time < self.end_time:
            return True
        return False

    def overlaps(self, other):
        """Check if this activity overlaps with another activity."""
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)

    def __str__(self):
        """String representation of the activity."""
        return f"{self.name} from {self.start_time}:00 to {self.end_time}:00"

class ActivityScheduler:
    def __init__(self):
        self.activities = []

    def add_activity(self, name, start_time, end_time):
        new_activity = Activity(name, start_time, end_time)
        if not new_activity.is_valid():
            print(f"Activity '{name}' has invalid time slots and was not added.")
            return

        for activity in self.activities:
            if new_activity.overlaps(activity):
                print(f"Activity '{name}' overlaps with '{activity.name}' and was not added.")
                return

        self.activities.append(new_activity)
        print(f"Activity '{name}' added successfully!")

    def list_activities(self):
        if not self.activities:
            print("No activities scheduled.")
        else:
            print("Scheduled Activities:")
            for activity in self.activities:
                print(activity)

# usage
def main():
    scheduler = ActivityScheduler()

    while True:
        print("\nMenu:")
        print("1. Add Activity")
        print("2. List Activities")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
                name = input("Enter activity name: ")
                start_time = float(input("Enter start time (24-hour format, e.g., 6.0 for 6:00 AM): "))
                end_time = float(input("Enter end time (24-hour format, e.g., 7.5 for 7:30 AM): "))
                scheduler.add_activity(name, start_time, end_time)
            
        elif choice == "2":
            scheduler.list_activities()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

