tasks = []


# function to add task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task {task} added successifuly")

# function to delete task
def delete_task():
    if not tasks:
        print("No tasks to delete")
        return
    
    print("Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}.{task}")

    try:
        task_index=int(input("Enter task number to delete: ")) -1
        if 0<=task_index< len(tasks):
            delete_task = tasks.pop(task_index)
        else:
            print("Invalid number entered no task deleted")
    except ValueError:
        print("Invalid input, please enter a valid task number")
        

    # function to view tasks
def view_task():
        if not tasks:
            print("No tasks to display")
        else:
            print("Tasks:")
            for index,task in enumerate(tasks):
                print(f"{index + 1}.{task}")
   
while True:
    print("\nTo-do list Application")
    print("1.Add task")
    print("2.Delete task")
    print("3.View task")
    print("4.Exit")

    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        view_task()
    elif choice == "4":
        print("Exiting Application, Goodbye!")
        break
    else:
        print("Invalid choice, please try again")