import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks in these satyam's list")
    print("2. Add task in these satyam's list")
    print("3. Delete task in these satyam's list")
    print("4. Exit in these satyam's list")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nTasks:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")

        elif choice == "2":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added!")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
                continue

            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")

            try:
                del_idx = int(input("Enter the task number to delete: ")) - 1
                if 0 <= del_idx < len(tasks):
                    removed = tasks.pop(del_idx)
                    save_tasks(tasks)
                    print(f"Deleted task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
