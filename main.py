#importing necessary files 
import add_contact
import remove_contact
import save_contacts
import view_contacts
import search_contact
import common_function

#list for storing the contacts
contacts=[] 

#before start reading data from file to list. 
save_contacts.read(contacts)

#changes 
 
def main_main():
    while(True):
        
        common_function.show_header("Contact Book Management System")

        print("1.Add contact\n2.Search contact\n3.Remove contact\n4.View contacts\n5.Exit")

        choice=input("Enter your choice : ")

        if choice=="1":
            add_contact.add(contacts)
        elif choice=="2":
            search_contact.search(contacts)
        elif choice=="3":
            remove_contact.remove(contacts)
        elif choice=="4":
            view_contacts.view(contacts)
        elif choice=="5":
            #before exit writing data from list to file.
            save_contacts.write(contacts)
            common_function.show_msg("Thank you for using Contact Book Management System !")
            break 
        else:
            common_function.show_msg("Invalid choice. Choose between 1 to 5.")

main_main() #calling main_menu 