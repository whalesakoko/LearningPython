#WEEK ONE ASSESMENT

import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")

        task = {
            "description": description,
            "due": due_date,
            "completed": False
        }

        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks):
                status = "Done" if task["completed"] else "pending"
                print(f"{i+1}. {task['description']} | Due: {task['due']} | {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task['description']} | Completed: {task['completed']}")
            
            try:
                num = int(input("Enter task number to mark complete: ")) - 1
                
                if 0 <= num < len(tasks):
                    tasks[num]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as complete!")
                else:
                    print("Invalid task number!")
                    
            except ValueError:
                print("Please enter a valid number")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task['description']}")

            try:
                num = int(input("Enter task number to delete: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['description']}")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number")


                

    elif choice == "5":
        break
    else:
        print("Invalid option") 