import csv



class Manager:

    def __init__(self):
        self.index = 0
        self.data = []
        with open('credentials.csv', "r") as file:
            reader = csv.reader(file)
            next(reader)
            for x in reader:
                self.data.append(x)
        
    

    def check_username_existance(self, entered_username):
        for line in self.data:
                    if line[1] == entered_username:
                        return True
        return False


    def add_user(self, entered_username):
        
                
                    
                    
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
                

                for i in self.data:
                    temp_id_list.append(i[0])

                for counter in range(len(temp_id_list)):
                    temp_username_list.insert(int(temp_id_list[counter])-1, self.data[counter][1])
                    

                temp_id_list.append(new_id)
                temp_id_list = [eval(i) for i in temp_id_list]
                temp_id_list = sorted(temp_id_list)
                temp_id_list = [str(i) for i in temp_id_list]

                for i in temp_id_list:
                    i = str(i)

                temp_username_list.insert(int(new_id)-1, entered_username)
                
                with open('credentials.csv', "wt") as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow(['ID','USERNAME'])
                    for counter in range(len(temp_id_list)):
                        writer.writerow([temp_id_list[counter],
                                            temp_username_list[counter]])
                        
                print('Written')
                return True
