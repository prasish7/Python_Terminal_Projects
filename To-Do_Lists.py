import json

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def remove_task(tasks, task_num):
    if 0 < task_num <= len(tasks):
        return tasks.pop(task_num - 1)
    else:
        return None
def display_tasks(tasks):
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
def main():
    tasks = load_tasks()
    is_running = True

    while is_running:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print(f'Task "{new_task}" added.')
        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter the task number to remove: "))
            removed_task = remove_task(tasks, task_num)
            if removed_task:
                save_tasks(tasks)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task number.")
        elif choice == '4':
            is_running = False
            print("Exiting To-Do List. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()