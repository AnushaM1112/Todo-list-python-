tasks = []

def show_menu():
    print("\n📝 To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added!")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        for i, t in enumerate(tasks):
            status = "✅" if t["done"] else "❌"
            print(f"{i+1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("🎉 Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ Task '{removed['task']}' deleted!")
    else:
        print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
