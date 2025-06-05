import base_tic_tac_toe as bTTT
import tasks
from utils import talk
import datetime
from utils import input_validation

def input_file_path():
    return input("Please insert file path for reading. I'll read the first two lines: ")

def edit_file():
    print("Entered the function edit_file")
    path = input_file_path()
    try:
        with open(path, 'r') as input_file:
            line1 = input_file.readline()
            line2 = input_file.readline()
            print("The first two lines are:", line1, line2)
    except Exception as e:
        print(f"Failed to read file: {e}")

def start_a_game():
    bTTT.TTT().mainloop()

def open_to_do_list():
    print("Welcome to the Microsoft To Do CLI")
    access_token: str = ""
    todo_list_id: str = ""
    
    todo_client = tasks.tasks(access_token)
    
    while True:
        print("\nChoose an option:")
        print("1. Show all tasks")
        print("2. Add a new task")
        print("3. Complete a task")
        print("4. Update a task")
        print("5. Set a reminder for a task")
        print("to exit type -1")
        
        choice = input("Your choice: ").strip()
        choice = str(input_validation(choice, lowerbound=0, upperbound=6))
        
        
        if choice == "-1":
            print("Exiting the To Do")
            break
        
        if choice == "1":
            # Refresh the list before printing
            tasks_list = todo_client.get_all_tasks(todo_list_id)
            todo_client.print_tasks(tasks_list)
            
        elif choice == "2":
            title = input("Enter task title: ").strip()
            body = input("Enter task description (optional): ").strip()
            new_task = todo_client.add_task(todo_list_id, title, body)
            if new_task:
                print("Task added successfully.")
            else:
                print("Failed to add task.")
        
        elif choice == "3":
            # Refresh and get only uncompleted tasks before printing
            tasks_list = todo_client.get_all_tasks(todo_list_id)
            filtered_tasks = todo_client.print_tasks(tasks_list, filter_status="uncompleted", return_filtered=True)
            if not filtered_tasks:
                print("No tasks available to complete.")
                continue
            try:
                task_number = int(input("Enter the task number to complete: ").strip())
                if 1 <= task_number <= len(filtered_tasks):
                    selected_task = filtered_tasks[task_number - 1]
                    print(f"You selected: {selected_task.get('title', 'No Title')}")
                    task_id = selected_task.get('id')
                    if todo_client.complete_task(todo_list_id, task_id):
                        print("Task completed successfully.")
                    else:
                        print("Failed to complete task.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            # Refresh tasks list before printing for update
            tasks_list = todo_client.get_all_tasks(todo_list_id)
            if not tasks_list:
                print("No tasks available to update.")
                continue
            todo_client.print_tasks(tasks_list)
            try:
                task_number = int(input("Enter the task number to update: ").strip())
                if 1 <= task_number <= len(tasks_list):
                    task_id = tasks_list[task_number - 1].get('id')
                    title = input("Enter new task title (press enter to skip): ").strip() or None
                    body = input("Enter new task description (press enter to skip): ").strip() or None
                    
                    updated_task = todo_client.update_task(todo_list_id, task_id, title, body)
                    if updated_task:
                        print("Task updated successfully.")
                    else:
                        print("Failed to update task.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "5":
            # Set a reminder for a task (using only uncompleted tasks)
            tasks_list = todo_client.get_all_tasks(todo_list_id)
            filtered_tasks = todo_client.print_tasks(tasks_list, filter_status="uncompleted", return_filtered=True)
            if not filtered_tasks:
                print("No tasks available to set reminders.")
                continue
            try:
                task_number = int(input("Enter the task number to set a reminder: ").strip())
                if 1 <= task_number <= len(filtered_tasks):
                    selected_task = filtered_tasks[task_number - 1]
                    minutes_from_now = int(input("Enter reminder time in minutes from now: ").strip())
                    phone_number = input("Enter the phone number (with country code) for WhatsApp reminder: ").strip()
                    todo_client.send_task_reminder(selected_task, minutes_from_now, phone_number)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        else:
            print("Invalid option, please try again.")