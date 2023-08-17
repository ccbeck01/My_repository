# This program logs in user and allows them to perform several actions. The user is able
# to log in with a username and password and is subsequently able to register other users.
# With a successful login, the user is also able to enter details of tasks and view details
# entered by all other registered users, as well as being able to view their details alone.

from datetime import date
result = 0

u_name = " "
p_word = " "
user_f = open("user.txt", "r+")
u_name_list = []
p_word_list = []
for line in user_f:
    sp_line = line.strip("\n").split(", ")
    u_name_list.append(sp_line[0])
    p_word_list.append(sp_line[1])
user_f.close()

u_name = input("Please enter your username: ")
p_word = input("Please enter your password: ")

while u_name not in u_name_list:
    print("\nYour username is incorrect. Please try again.")
    u_name = input("\nPlease enter your username: ")
    p_word = input("Please enter your password: ")
position = u_name_list.index(u_name)

while p_word != p_word_list[position]:
    print("\nYour password is incorrect. Please try again.")
    p_word = input("\nPlease enter your password: ")
while p_word == p_word_list[position]:
    print(f"\nHi {u_name}, you are logged in now!")
    result = 1
    break


# This block presents the menu after the login details have been validated.
while result == 1:
    menu = input('''\nSelect one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit: ''').lower()

# In this block the user has chosen to register a user. It requests the input of
# the username and password. After confirming the password, the login details are
# written to a txt file.

    if menu == 'r':
        result = 0
        while result <= 2:
            u_name = input("\nPlease enter the username:\n")
            p_word = input("Please enter the password:\n")
            p_word_match = input("Please enter your password again.\n")
            if p_word_match == p_word:
                f = open("user.txt", "a")
                f.write("\n" + u_name + ", " + p_word)
                f.close()
                break
            elif p_word_match != p_word:
                print("The passwords you have entered do not match. Try again.")
                result += 1
            if result > 2:
                print("Please contact the administrator for assistance.")
        result = 1

# This set of instructions, allows the user to add a set of tasks to the txt file.

    elif menu == 'a':
        u_name = input("\nPlease enter your user name:\n")
        title = input("What is the title of the task?: \n")
        desc = input("Give a short description of the task:\n")
        due_date = input("Please enter the due date of the task dd/mm/yyy:\n")
        curr_date = str(date.today())
        task_complete = input("Is the task complete?: Yes / No\n")
        f = open("tasks.txt", "a")
        f.write(u_name + ", ")
        f.write(title + ", ")
        f.write(desc + ", ")
        f.write(due_date + ", ")
        f.write(curr_date + ", ")
        f.write(task_complete + " ")
        f.close()
        result = 1

# This set of instructions prints out all tasks written to the txt file.

    elif menu == 'va':
        print("\n\n_______________________________List of all tasks_____________________________\n")
        f = open("tasks.txt", "r+")
        for line in f:
            split_line = line.split(", ")
            print(f"Task:\t\t\t\t\t{split_line[1]}")
            print(f"Assigned to:\t\t\t{split_line[0]}")
            print(f"Date assigned:\t\t\t{split_line[4]}")
            print(f"Due date:\t\t\t\t{split_line[3]}")
            print(f"Task complete?:\t\t\t{split_line[5]}")
            print(f"Task description:\n{split_line[2]}")
            print("______________________________________________________________________________\n")
        result = 1
        f.close()

# This set of instructions prints out tasks written to the txt file, by a particular
# user only

    elif menu == 'vm':
        print("\n______________________________________My tasks__________________________________\n")
        f = open("tasks.txt", "r")
        uname = " "
        for line in f:
            split_line = line.split(", ")
            if split_line[0] == u_name:
                print(f"Task:\t\t\t\t\t{split_line[1]}")
                print(f"Assigned to:\t\t\t{split_line[0]}")
                print(f"Date assigned:\t\t\t{split_line[4]}")
                print(f"Due date:\t\t\t\t{split_line[3]}")
                print(f"Task complete?:\t\t\t{split_line[5]}")
                print(f"Task description:\n{split_line[2]}")
                print("______________________________________________________________________________\n")
        result = 1
        f.close()

# This allows the user to exit the menu.

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

# This error message is printed out if the selected character is not on the menu.

    else:
        print("You have made a wrong choice, Please Try again")

