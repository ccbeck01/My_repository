# This program logs in user and allows them to perform several actions. The user is able
# to log in with a username and password and is subsequently able to register other users.
# With a successful login, the user is also able to enter details of tasks and view details
# entered by all other registered users, as well as being able to view their details alone.


# Thanks for the feedback.  Unfortunately time will not permit me to make all the corrections.  I have to 
# move on to try and cover some more tasks. Hopefully soon.


from datetime import date

import datetime

# This function opens a text file and returns its content. It returns 2 sets of data:
# data contains all columns and usname_data contains only usernames of the users


def read_file(txtfile):
    data = []
    usname_data = []
    f = open(txtfile, "r")
    for line in f:
        sp_line = line.strip("\n").split(", ")
        data.append(sp_line)
        usname_data.append(sp_line[0])
    return data, usname_data


# This function requests the username and password from the user at login and returns them.

def get_details():

    data = read_file("user.txt")[0]

    u_name = input("\nPlease enter the username: ")
    p_word = input("\nPlease enter the password: ")

    try:
        for line in data:
            if line[0] == u_name and line[1] == p_word:
                return u_name, p_word

    except ValueError:
        print("\nYour details are not registered. Please enter a valid username.")


# This function receives the name of a text file, the username and password of the user. It then opens a text
# file and writes these details into it

def writeto_file(txtfile, usr_name, pss_word):
    usr_name, pss_word = get_details()
    f = open(txtfile, "a")
    f.write("\n" + usr_name + ", " + pss_word)
    f.close()


# This function registers a user to the system.

def reg_user():
    uname, pword = get_details()
    uname_list = read_file("user.txt")[1]

    while uname in uname_list:
        print("This user name is already in use. Try another user name.")
        break

    while uname not in uname_list:

        pword_match = input("Please enter your password again.\n")
        if pword != pword_match:
            print("Your passwords do not match. Try again.")
            break
        else:
            writeto_file("user.txt", uname, pword)
            print("Thank you. The user's details have been saved.")
            break


# This block asks the user to enter task details , which are then written to a txt file.

def add_task():
    ad_name = input("\nPlease enter your user name:\n")
    title = input("What is the title of the task?: \n")
    desc = input("Give a short description of the task:\n")
    due_date = input("Please enter the due date of the task yyyy-mm-dd:\n")
    curr_date = str(date.today())
    task_complete = input("Is the task complete?: Yes / No\n")

    f = open("tasks.txt", "a")
    f.write(ad_name + ", ")
    f.write(title + ", ")
    f.write(desc + ", ")
    f.write(due_date + ", ")
    f.write(curr_date + ", ")
    f.write(task_complete)
    f.write("\n")
    f.close()


# This set of instructions prints out all tasks written to the txt file.

def view_all():
    print("\n\n______________________________List of all tasks______________________________\n")
    f = open("tasks.txt", "r+")
    for line in f:
        split_line = line.split(", ")
        print(f"Task:\t\t\t\t\t{split_line[1]}")
        print(f"Assigned to:\t\t\t{split_line[0]}")
        print(f"Date assigned:\t\t\t{split_line[4]}")
        print(f"Due date:\t\t\t\t{split_line[3]}")
        print(f"Task complete?:\t\t\t{split_line[5]}")
        print(f"Task description:\n{split_line[2]}")
        print("\n______________________________________________________________________________\n")
    f.close()


# This set of instructions prints out tasks written to the txt file, belonging the logged-in user only.

def view_mine(vm_name):

    positions = []

    data = read_file("tasks.txt")[0]  # data collected from the tasks file.

    for line in data:                       # iterating through the lines of data to match the username to their indices
        if line[0] == vm_name:              # below the positions/indices identifying the user are formatted for the
            position = data.index(line)     # text file.
            positions.append(position)

            print(f"\n__________________________________Task no.{position}____________________________________\n")
            print(f"Task:\t\t\t\t\t{line[1]}")
            print(f"Assigned to:\t\t\t{line[0]}")
            print(f"Date assigned:\t\t\t{line[4]}")
            print(f"Due date:\t\t\t\t{line[3]}")
            print(f"Task complete?:\t\t\t{line[5]}")
            print(f"Task description:\n{line[2]}")


# line[5] tells if the task is complete or not. This block is selecting the uncompleted tasks belonging to the user.

    for line in data:
        if line[0] == vm_name and line[5].lower() != "yes":
            task_num = int(input(f"\nEnter the task number you would like to edit {positions} or enter -1 to exit: "))

            for line in data:
                if task_num == data.index(line):
                    edit_line = data[task_num]

# Now that the uncompleted tasks have been selected, the user has the option to edit or mark it as complete.

                    while edit_line[5].strip(" ").lower() == "no":
                        edit_choice = input('''\nSelect one of the following options:
                                        mc - mark task as complete
                                        ed - edit task: ''').lower()

                        if edit_choice == "mc":
                            edit_line[5] = "Yes\n"
                            data[task_num] = edit_line

                            with open("tasks.txt", "w") as f:
                                for line in data:
                                    line = ", ".join(line)
                                    f.write(line + "\n")

                            print(f"\nThank you. Task {task_num} has been marked complete. Good bye!!")
                            break

# the uncompleted task selected can be edited by changing the username, due date or marking it as complete.

                        elif edit_choice == "ed":
                            new_choice = input('''\nSelect one of the following options:
                                            cd - change due date
                                            cn - change user name: ''').lower()

                            if new_choice == "cd":
                                new_due_date = input("\nEnter new due date yyyy-mm-dd: ")
                                edit_line[3] = new_due_date
                                data[task_num] = edit_line

                                with open("tasks.txt", "w") as f:
                                    for line in data:
                                        line = ", ".join(line)
                                        f.write(line + "\n")

                                print(f"\nThank you. Task {task_num} has been marked complete. Good bye!!")
                                break

                            elif new_choice == "cn":
                                new_user_name = input("\nEnter new user name: ")
                                edit_line[0] = new_user_name
                                data[task_num] = edit_line

                                with open("tasks.txt", "w") as f:
                                    for line in data:
                                        line = ", ".join(line)
                                        f.write(line + "\n")

                                print(f"\nThank you. Task {task_num} has been edited. Good bye!!")

                                break

                    while edit_line[5].lower() == "yes":
                        print("\nThis task has already been marked complete.")
                        break

# This function calculates the total number of tasks that have been generated and tracked
# using the task_manager.py and returns the value.


def total_tasks():
    task_total = 0
    tasks = read_file("tasks.txt")[0]

    for line in tasks:
        task_total += 1

    return task_total


# This function finds the total number of completed and uncompleted tasks and returns the values.

def tasks_complete():
    completed = 0
    uncompleted = 0
    tasks = read_file("tasks.txt")[0]

    for line in tasks:
        if line[5].lower() == "yes":
            completed = completed + 1

        elif line[5].lower() == "no":
            uncompleted += 1

    return completed, uncompleted


# This function calculates the total number of tasks that haven’t been completed and are overdue.

def uncompleted_overdue():
    tasks = read_file("tasks.txt")[0]
    tasks_overdue = 0

    for task in tasks:
        if task[5].lower() == "no":
            due_date = str(task[3])

            date_format = "%Y-%m-%d"
            obj_today = datetime.datetime.today()
            obj_due_date = datetime.datetime.strptime(due_date, date_format)

            if obj_due_date > obj_today:
                tasks_overdue += 1

    return tasks_overdue


# This function calculates and returns the percentage of tasks that are incomplete.

def percentage_incomplete():
    num_tasks = total_tasks()
    num_incomplete = tasks_complete()[0]

    perc_incomplete = float(num_incomplete / num_tasks * 100)

    return perc_incomplete


# This function calculates and returns the percentage of tasks that are overdue.

def percentage_overdue():
    num_tasks = total_tasks()
    num_overdue = uncompleted_overdue()

    perc_overdue = float(num_overdue / num_tasks * 100)

    return perc_overdue


# This function generates reports and writes them to a text file.

def generate_reports():
    with open("task_overview.txt", "w+") as f:
        f.write("\n________________Task Management Statistics - Tasks_________________")
        f.write(f"\n\nTotal number of tasks generated:\t\t\t{total_tasks()}")
        f.write(f"\n\nTotal number of completed tasks: \t\t\t{tasks_complete()[0]}")
        f.write(f"\n\nTotal number of uncompleted tasks: \t\t\t{tasks_complete()[1]}")
        f.write(f"\n\nNumber of uncompleted and overdue tasks: \t{uncompleted_overdue()}")
        f.write(f"\n\nPercentage of incomplete tasks: \t\t\t{percentage_incomplete()}%")
        f.write(f"\n\nPercentage of overdue tasks: \t\t\t\t{percentage_overdue()}%")

        f.write("\n\n\n________________Task Management Statistics - Users_________________")
        f.write(f"\n\nTotal number of users: t\t\t\t\t\t\t{user_total()}")
        f.write(f"\n\nTotal number of tasks generated:\t\t\t\t{total_tasks()}")
        f.write(f"\n\nTotal number of tasks generated for a user:\t\t{users_tasks()}")


# This function calculates and returns the total number of users

def user_total():
    all_users = read_file("user.txt")[0]
    total_users = 0
    total_users = len(all_users)
    return total_users


# This function calculates the total number of tasks assigned to a user.

def users_tasks():
    all_users = read_file("user.txt")[0]
    tasks = read_file("tasks.txt")[0]
    uname = " "
    new_user = []
    new_user_tsk = []
    dict_user_task = {}

    i = 0
    for user in all_users:
        uname = user[0]
        for task in tasks:
            if uname == task[0]:
                i = task.count(task[0])
                new_user.append(uname)
                new_user_tsk.append(i)

            print(task[0])
            print(i)

    print(new_user)
    print(new_user_tsk)
    name = ""
    i = 1
    for i in range(1, len(new_user)):
        name = new_user[0]
        num_task = new_user.count(name)
        i += 1
        print(name, num_task)

    return new_user, new_user_tsk


# This function exits the menu.

def exit_menu():
    print('Goodbye!!!')
    exit()


# This function presents the main menu of the program, which gives options for different processes. It first
# validates the user's details and if they are correct, the user is allowed to proceed with performing other
# functions.

def func_menu():

    u_name, p_word = get_details()

    while True:

        menu = input('''\nSelect one of the following options below:
                    r - registering a user
                    a - add a task
                    va - view all tasks
                    vm - view my tasks
                    gr - generate reports
                    ds - display statistics
                    e - Exit: ''').lower()

        if menu == "r" and u_name == "admin":
            reg_user()

        elif menu == "a":
            add_task()

        elif menu == "vm":
            view_mine(u_name)

        elif menu == "va":
            view_all()

        elif menu == "gr":
            generate_reports()

        elif menu == 'e':
            exit_menu()

        else:
            print("\nYou have made a wrong choice, Please Try again.")

# This statement is calling the main menu.


func_menu()
user_total()
users_tasks()
generate_reports()
