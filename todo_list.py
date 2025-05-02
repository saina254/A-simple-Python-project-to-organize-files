# Create an empty list to store tasks
tasks = []

# Show menu in a loop
while True:
    print("\n==== TO-DO LIST MENU ====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")
    
    elif choice == '2':
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == '3':
        task_number = int(input("Enter the task number to delete: "))
        if 0 < task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter a number from 1 to 4.")
