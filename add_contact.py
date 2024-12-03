#importing necessary files 
import common_function 
import validation

#function for adding contact
def add(contacts):
    common_function.show_header("Add Contact")
    
    #taking input 
    #strip()-> removing leading and trailling spacess,newlines and tabs 
    #name 
    while True:
        name = input("Enter your name : ").strip() 
        if(validation.validate_name(name)):
            break
    #email 
    while True:
        email = input("Enter your email : ").strip()  
        if(validation.validate_email(email)):
            break
    #phone_number 
    while True:
        phone_number = input("Enter your phone number : ").strip() 
        if(validation.validate_phn_num(contacts,phone_number)):
            break
    #address 
    while True:
        address = input("Enter your address : ").strip() 
        if(validation.validate_address(address)):
            break   

    #making dictionary  
    contact = {
        "name" : name,
        "email" : email,
        "phone_number" : phone_number,
        "address" : address
    }
    contacts.append(contact) #adding dictionary to list 
    common_function.show_msg("Contact added successfully.")