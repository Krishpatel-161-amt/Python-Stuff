import sys
# fixes utf-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# empty list for tasks
daily_tasks = []

# loops the menu forever
while True:
    # prints menu options
    print("=== My Daily Lists ===")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Quit")

    # asks for choice
    user_choice = input("Choose an option: ")
    
    # checks if view tasks
    if user_choice == "1":
        # loops through tasks
        for task in daily_tasks:
            # prints each task
            print(task)
            
    # checks if add task
    elif user_choice == "2":
        # asks for new task
        add_task = input("What is the new task? ")
        # adds task to list
        daily_tasks.append(add_task)
        
    # checks if remove task
    elif user_choice == "3":
        # asks for task to remove
        remove_task = input("Which task to remove? ")
        # checks if task exists
        if remove_task in daily_tasks:
            # removes the task
            daily_tasks.remove(remove_task)
        else:
            # prints error message
            print("Task not found.")
            
    # checks if quit
    elif user_choice == "4":
        # exits menu
        print("Exiting the menu...")
        break
        
    else:
        # handles bad input
        print("Invalid choice, please pick a number from 1-4")
