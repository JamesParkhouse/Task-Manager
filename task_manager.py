'''A program that takes login credentials from a user, presents a 
menu of task management options, and executes appropriate actions for
the selected option.'''

#====Login Section====

# Create dictionary of credentials and
# populate with details from text file. 
credentials = {}
with open('user.txt', 'r') as f:
    for line in f:
        username, password = line.strip().split(', ')
        credentials[username] = password

# Verify username, and if valid
# verify password
while True:
    username = input("Enter your username: ")
    if username not in credentials:
        print("Invalid username. Please try again.")
    else:
        password = input("Enter your password: ")
        if credentials[username] != password:
            print("Incorrect password. Please try again.")
        else:
            print("\nLogin successful.\n")
            break

#=======Task Management Section========
while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''
Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit

Enter selection: ''').lower()
    
    if menu == 'r':
        # Take user inputs for new user details. Confirm password before 
        # writing new credentials to text file. 
        while True:
            new_username = input("Enter new user's username: ")
            new_password = input("Enter new user's password: ")
            confirm_password = input("Confirm password: ")
            if confirm_password == new_password:
                with open('user.txt', 'a') as f:
                    f.write("\n" + new_username + ", " + new_password)
                    break
            else:
                print("Passwords do not match. Please check and reenter")
            
    elif menu == 'a':
        # Take user inputs for details of new task, and write to file.
        print("Enter the following details about the task:\n")
        assigned_user = input("Username task is assigned to: ")
        title = input("Title of assigned task: ")
        description = input("Description of task: ")
        date_assigned = input("Current date (dd Mon yyyy): ")
        due_date = input("Due date for task (dd Mon yyyy): ")
        with open('tasks.txt', 'a') as f:
            f.write(f'''
{assigned_user}, {title}, {description}, {date_assigned}, {due_date}, No''')

    elif menu == 'va':
        # Read task details from file and print in readable format.
        with open('tasks.txt', 'r') as f:
            for line in f:
                task_details = line.strip().split(', ')
                print(f'''
        Task:\t\t {task_details[1]}
        Assigned to:\t {task_details[0]}
        Date assigned:\t {task_details[3]}
        Due date:\t {task_details[4]}
        Task Complete?\t {task_details[5]}
        Task description:\n\t {task_details[2]}\n''')
            
    elif menu == 'vm':
        # Read task details from file. If first index in task details 
        # list is the same as login username, print task details. 
        with open('tasks.txt', 'r') as f:
            for line in f:
                task_details = line.strip().split(', ')
                if task_details[0] == username:
                    print(f'''
        Task:\t\t {task_details[1]}
        Assigned to:\t {task_details[0]}
        Date assigned:\t {task_details[3]}
        Due date:\t {task_details[4]}
        Task Complete?\t {task_details[5]}
        Task description:\n\t {task_details[2]}\n''')
            
    elif menu == 'e':
        print('Exiting program. Goodbye.')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
