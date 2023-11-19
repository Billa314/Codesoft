#Muhammad Bilal
#To_Do_list
#CodSoft Internshipp Task
# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to display all tasks in the list
def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task index. Please provide a valid task number.")
    except ValueError:
        print("Invalid input. Please enter a task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        task_index = input("Enter the task number to remove: ")
        remove_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
