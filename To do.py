FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.")
    else:
        print("Task cannot be empty.")
    return input("What do you want to do next? (add/remove/view/quit): ").strip().lower()

def remove_task(tasks):
    task = input("Enter the task to remove: ").strip()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")
    return input("What do you want to do next? (add/remove/view/quit): ").strip().lower()

def view_tasks(tasks):
    if tasks:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")
    return input("What do you want to do next? (add/remove/view/quit): ").strip().lower()

def main():
    tasks = load_tasks()
    action = input("What do you want to do? (add/remove/view/quit): ").strip().lower()
    while action != "quit":
        if action == "add":
            action = add_task(tasks)
        elif action == "remove":
            action = remove_task(tasks)
        elif action == "view":
            action = view_tasks(tasks)
        else:
            print("Invalid option. Please choose 'add', 'remove', 'view', or 'quit'.")
            action = input("What do you want to do next? (add/remove/view/quit): ").strip().lower()

if __name__ == "__main__":
    main()  