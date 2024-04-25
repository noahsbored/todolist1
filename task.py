tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {'[X]' if task['completed'] else '[ ]'} {task['task']}")

def mark_task_complete(task_index):
    if 1 <= task_index  <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task deleted.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nMenu:")
        print("1. add task")
        print("2. view tasks")
        print("3. mark a task as complete")
        print("4. delete a task")
        print("5. quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("enter task description: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_index = int(input("enter the index of the task to mark as complete: "))
            mark_task_complete(task_index)
        elif choice == "4":
            task_index = int(input("enter the index of the task to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("exiting.")
            break
        else:
            print("invalid choice. Please enter a number between 1 and 5.")

main()
