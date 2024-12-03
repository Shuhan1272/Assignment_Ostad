#importing necessary function 
import common_function

#function for display all the contacts
def view(contacts):
    common_function.show_header("View Contacts")

    if(len(contacts)==0):
        common_function.show_msg("No contact to display.")
    else:
        #displaying contact 
        for contact in contacts:
            contact_str=""
            for key,value in contact.items():
                contact_str+=(key.title()+" : "+value+" | ")
            common_function.show_msg(contact_str.removesuffix(" | "))

