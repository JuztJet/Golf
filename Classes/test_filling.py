import csv

# id:    ,username:
#
#
#
#

class Text_Filling:
    def __init__(self):
        self.index = 0
        self.data = []
        with open('test.csv', "r") as file:
            reader = csv.reader(file)
            next(reader)
            for x in reader:
                self.data.append(x)

    def main_menu(self):
        print('<================== Hello, please login to TEST_SERVICE Service ==================>')
        print('<=================== If you would like to quit at anytime, enter q ==================>')

        login_or_quit = ''

        while login_or_quit != 'l':
            login_or_quit = input("Enter 'l' to login: ")
            self.quit_detection(login_or_quit)

            if login_or_quit == 'l':
                print('Proceeding to login menu')
                print("<=================== Welcome to login page ===================>")
                self.login_menu()
            else:
                print("Please enter 'l' to login or 'q' to quit")

    def login_menu(self):

        username = input('Please enter your username: pluh')
        self.quit_detection(username)
        self.check_username_password(username)
    def check_username_password(self, username):
        for line in self.data:
            if username==line[1]:
                password = ''
                password = input('Enter Password: ')
                self.quit_detection(password)
                while password != line[2]:

                    print('Incorrect Password')
                    password = input('Enter Password: ')
                    self.quit_detection(password)

                print('Access granted, welcome', username, ', id:', line[0])
                self.index = self.data.index(line)

                self.options()
                return
        print('Incorrect Username')
        self.login_menu()

    def options(self):
        print("<=================== Welcome to the interface, please choose an option ===================>")
        print("1. Enter 'view_self' to view your details \n",
                 "2. Enter 'change_pass' to change your password \n",
                 "3. Enter 'add_user' to add an user to the file (admin needed) \n",
                 "4. Enter 'home' to return home\n")
        choice = input()
        self.quit_detection(choice)
        while choice != 'view_self' and choice != 'change_pass' and choice != 'add_user' and choice != 'home':
            print('Invalid option, enter option: ')
            choice = input()
            self.quit_detection(choice)
        if choice == 'change_pass':
            self.change_pass()
        elif choice == 'view_other':
            pass
        elif choice == 'add_user':
            self.add_user()
        else:
            self.main_menu()
    def change_pass(self):
        print("<=================== Change password menu ===================>")
        print("If you would like to continue, enter 'c'. To return to interface, enter 'e'")
        choice = input()
        self.quit_detection(choice)
        print(choice)
        while choice != 'c' and choice != 'e':
            print('Invalid option')
            print("If you would like to continue, enter 'c'. To return to interface, enter 'e'")
            choice = input()
        if choice == 'e':
            self.options()
        else:
            initial_chosen_password = input('Enter new password: ')
            safety_chosen_password = input('Please enter the password again: ')
            while initial_chosen_password!=safety_chosen_password:
                print("Passwords don't match")
                initial_chosen_password = input('Enter new password: ')
                safety_chosen_password = input('Please enter the password again: ')
            chosen_password = safety_chosen_password

            temp_id_list = []
            temp_username_list = []
            temp_password_list = []
            temp_admin_choice_list = []
            for counter in range(len(self.data)):
                temp_id_list.append(self.data[counter][0])
                temp_username_list.append(self.data[counter][1])
                if counter == self.index:
                    temp_password_list.append(chosen_password)
                    print(2000)
                else:
                    temp_password_list.append(self.data[counter][2])
                temp_admin_choice_list.append(self.data[counter][3])
            with open('test.csv', "wt") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(['ID', 'USERNAME', 'PASSWORD', 'ADMIN'])
                for counter in range(len(temp_id_list)):
                    writer.writerow([temp_id_list[counter],
                                     temp_username_list[counter],
                                     temp_password_list[counter],
                                     temp_admin_choice_list[counter]])
            print('Written')
            print('Returning to interface...')
            self.options()
            return


    def add_user(self):
        print("<=================== Add new user menu ===================>")
        print("If you would like to continue, enter 'c'. To return to interface, enter 'e'")
        choice = input()
        self.quit_detection(choice)
        print(choice)
        while choice != 'c' and choice != 'e':
            print('Invalid option')
            print("If you would like to continue, enter 'c'. To return to interface, enter 'e'")
            choice = input()
        if choice == 'e':
            self.options()
        else:
            lock_1 = True
            lock_3 = True

            print('Checking for admin privileges')
            print('...')
            print('...')
            if self.data[self.index][3] == "False":
                print('No admin privileges on this user, returning to interface...')
                self.options()
            print('Admin privileges found')

            chosen_username = input('Enter username of to-be-created user')
            while lock_1:
                lock_2 = False
                print('Checking if username is available')


                for line in self.data:
                    print('...')
                    if line[1] == chosen_username:
                        print('Username unavailable')
                        lock_2 = True
                if lock_2:
                    chosen_username = input('Enter username of to-be-created user')
                else:
                    lock_1 = False
                    print('Username available')
                    chosen_password = input('Please enter the password')
                    admin_option = ''

                    admin_option = input("Please enter 'True', to make the user an admin, or 'False', to not make the user an admin")
                    while admin_option != 'True' and admin_option != 'False':
                        print('Invalid option')
                        admin_option = input(
                            "Please enter 'True', to make the user an admin, or 'False', to not make the user an admin")
                    print('Creating an ID...')

                    new_id = False
                    lock_4 = True
                    temp_list = []
                    for i in range(len(self.data)):

                        temp_list.append(self.data[i][0])


                    temp_list = [eval(i) for i in temp_list]

                    temp_list = sorted(temp_list)
                    temp_list = [str(i) for i in temp_list]


                    for i in range(len(self.data)):

                        if str(i + 1) != temp_list[i]:
                            print('Gap found!')
                            new_id = i+1
                            lock_4 = False
                        if not lock_4:
                            break
                    if new_id == False:
                        new_id = len(self.data)+1
                    new_id = str(new_id)
                    print('New ID :', new_id)

                    temp_id_list = []
                    temp_username_list = []
                    temp_password_list = []
                    temp_admin_choice_list = []

                    for i in self.data:
                        temp_id_list.append(i[0])




                    for counter in range(len(temp_id_list)):
                        temp_username_list.insert(int(temp_id_list[counter])-1, self.data[counter][1])
                        temp_password_list.insert(int(temp_id_list[counter])-1, self.data[counter][2])
                        temp_admin_choice_list.insert(int(temp_id_list[counter])-1, self.data[counter][3])

                    temp_id_list.append(new_id)

                    temp_id_list = [eval(i) for i in temp_id_list]



                    temp_id_list = sorted(temp_id_list)
                    temp_id_list = [str(i) for i in temp_id_list]
                    for i in temp_id_list:
                        i = str(i)
                    temp_username_list.insert(int(new_id)-1, chosen_username)
                    temp_password_list.insert(int(new_id)-1, chosen_password)
                    temp_admin_choice_list.insert(int(new_id)-1, admin_option)



                    with open('test.csv', "wt") as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow(['ID','USERNAME','PASSWORD','ADMIN'])
                        for counter in range(len(temp_id_list)):
                            writer.writerow([temp_id_list[counter],
                                             temp_username_list[counter],
                                             temp_password_list[counter],
                                             temp_admin_choice_list[counter]])
                    print('Written')
                    print('Returning to interface...')
                    self.options()
                    return



    def quit_detection(self, input):
        if input == 'q':
            exit(print('Quiting...'))
    def update(self):
        #self.main_menu()
        self.change_pass()

test_filling_1 = Text_Filling()
test_filling_1.update()
















# with open('test.csv', 'a') as file:
#     fieldnames = ['id', 'username', 'password']
#     writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
#     writer.writerow({'id': "0001", 'username': "John Doe", 'password': 20})
