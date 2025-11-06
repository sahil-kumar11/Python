tasks = []

def add_task():
    task_text = input("Enter your task: ")

    task_dict = {
        "task_name": task_text,
        "status" : "pending"
    }

    tasks.append(task_dict)

    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks added.")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task['task_name']} - {task['status']}")


def mark_task_complete():
    if not tasks:
        print("No tasks to mark as complete.")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task['task_name']} - {task['status']}")

    task_number = int(input("Enter task number: "))
    if 1 <= task_number <=  len(tasks):
        tasks[task_number - 1]["status"] = "completed"
        print("Task completed.")
    else:
        print("Task not found.")

def delete():
    if not tasks:
        print("No tasks to delete.")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task['task_name']} - {task['status']}")

        task_delete = int(input("Enter the task number you want to delete: "))
        if 1 <= task_delete <= len(tasks):
            del tasks[task_delete - 1]
            print("Task deleted.")
        else:
            print("Invalid task.")


while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    number_enter = int(input("Please select an option (1-5): "))

    if number_enter == 1:
        add_task()
    elif number_enter == 2:
        view_tasks()
    elif number_enter == 3:
        mark_task_complete()
    elif number_enter == 4:
        delete()
    elif number_enter == 5:
        print("Exiting Task Manager......")
        break
    else:
        print("Invalid input.")
