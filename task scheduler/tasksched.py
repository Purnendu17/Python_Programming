class Task:
    def __init__(self, name, priority, duration, deadline_day):
        self.name = name
        self.priority = priority
        self.duration = duration
        self.deadline_day = deadline_day

class TaskNode:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = TaskNode(task)
        if not self.head:
            self.head = new_node
        else:
            # Insert at end
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_sorted_tasks(self):
        # Convert linked list to list for sorting
        tasks = []
        current = self.head
        while current:
            tasks.append(current.task)
            current = current.next
        # Sort: first by priority (lower is higher), then by deadline_day (earlier = more urgent)
        tasks.sort(key=lambda t: (t.priority, t.deadline_day))
        return tasks

def schedule_tasks():
    task_list = TaskList()

    num_days = int(input("Enter number of days in the month (e.g., 30): "))
    num_tasks = int(input("Enter number of tasks to schedule: "))

    for i in range(num_tasks):
        print(f"\nEnter details for Task {i+1}:")
        name = input("Task Name: ")
        priority = int(input("Priority (lower number = higher priority): "))
        duration = int(input("Duration (in hours): "))
        deadline_day = int(input("Deadline Day (1 to {}): ".format(num_days)))
        task = Task(name, priority, duration, deadline_day)
        task_list.add_task(task)

    sorted_tasks = task_list.get_sorted_tasks()

    print("\n--- Monthly Task Schedule ---")
    for day in range(1, num_days + 1):
        print(f"\nDay {day}:")
        day_tasks = [t for t in sorted_tasks if t.deadline_day == day]
        if day_tasks:
            for t in day_tasks:
                print(f"  → Task: {t.name} | Priority: {t.priority} | Duration: {t.duration} hrs | Deadline: Day {t.deadline_day}")
                if t.deadline_day == day:
                    print("     ⚠️  URGENT: Deadline is today!")
        else:
            print("  No tasks scheduled.")

# Run it
schedule_tasks()
