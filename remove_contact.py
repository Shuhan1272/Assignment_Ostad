#importing necessary files 
import common_function

#function  for removing contact 
def remove(contacts):
    #searching for the contact want to remove based on phone number
    common_function.show_header("Remove Contact")

    phone_number=input("Enter the phone number : ") #taking input
    matched_index=common_function.get_matched_index(contacts,phone_number) #search 

    if matched_index == -1: 
        common_function.show_msg("No such contact exist.")
    else:
        contacts.pop(matched_index) #removing
        common_function.show_msg("Contact deleted successfully.")


