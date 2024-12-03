#importing necessary function 
import common_function

#function writing data from list to file 
def write(contacts):
    try:
        with open("contacts.text","w") as file:
            for contact in contacts:
                for value in contact.values():
                    file.write(value+' ')
                file.write('\n') #newline write
    except Exception as e:
        common_function.show_msg(str(e))

#function reading data from file to list 
def read(contacts):
    try:
        with open("contacts.text","r") as file:
            for line in file:
                data_list=line.split(' ')
                
                #making dictionary  
                contact = {
                    "name" : data_list[0],
                    "email" : data_list[1],
                    "phone_number" : data_list[2],
                    "address" : data_list[3]
                }
                contacts.append(contact)
    except Exception as e:
        common_function.show_msg(str(e))