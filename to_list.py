import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("To-Do List Application")
    print("----------------------")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Quit")
    print()

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "Completed" if completed else "Not Completed"
            print(f"{i}. {task} [{status}]")
    print()

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append((task, False))
    print(f"Task '{task}' has been added.")
    print()

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks[task_num - 1]
            tasks[task_num - 1] = (task, True)
            print(f"Task '{task}' has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    print()

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task, _ = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    print()

def main():
    tasks = []
    while True:
        clear_screen()
        display_menu()
        choice = input("Choose an option (1-5): ")
        print()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
