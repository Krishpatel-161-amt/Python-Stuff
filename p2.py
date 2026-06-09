daily_tasks = []

#Infinite Loop for menu
while True:
    print("===My Daily Lists===")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Quit")

    # For user choice
    user_choice = input("Choose an option: ")
    
    # for Option 1(Viewing tasks)
    if user_choice == "1":
        for task in daily_tasks:
            print(task)
    
    # for Option 2 (adding tasks)
    elif user_choice == "2":
        add_task = input("What is the new task?")
        daily_tasks.append(add_task)
    
    # for Option 3 (removing tasks)
    elif user_choice == "3":
        remove_task = input("Which task to remove?")
        daily_tasks.remove(remove_task)
    
    # For Option 4 (Exit the menu)
    elif user_choice == "4":
        print("Exiting the menu...")
        break

    # for catching errors    
    else:
        print("Invalid choice, please pick a number from 1-4")
