def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task description: ")
    if task:
        task_id = len(tasks) + 1
        tasks[task_id] = task
        print(f"Task {task_id} added.")
    else:
        print("Task cannot be empty.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"{task_id}. {task}")

def remove_task(tasks):
    try:
        task_id = int(input("Enter the task ID to remove: "))
        if task_id in tasks:
            del tasks[task_id]
            print(f"Task {task_id} removed.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = {}
    while True:
        display_menu()
        choice = input("Choose an option (1/2/3/4): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
