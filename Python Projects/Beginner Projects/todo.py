TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter a new task: ").strip()
    if not task:
        print("No task entered. Nothing added.")
        return
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ").strip())
    except ValueError:
        print("Please enter a valid number.")
        return
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' deleted.")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\n==== To-Do Menu ====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting. Bye.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
