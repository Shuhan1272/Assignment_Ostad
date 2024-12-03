#importing necessary files 
import common_function

#function for searching contact    
def search(contacts):
    common_function.show_header("Search Contact")
    
    #searching for the contact based on phone number  
    phone_number=input("Enter the phone number : ") #taking input
    matched_index=common_function.get_matched_index(contacts,phone_number) #search

    if matched_index == -1:
        common_function.show_msg("No such contact exist.")
    else:
        #contact found. displaying contact.
        contact_str=""
        for key,value in contacts[matched_index].items():
            contact_str+=(key.title()+" : "+value+" | ")

        common_function.show_msg("Contact found.")
        common_function.show_msg(contact_str.removesuffix(" | "))


