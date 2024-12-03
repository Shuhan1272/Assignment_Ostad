#importing necessary files 
import common_function

#input fields validation during add.
"""
Common validation : Space is not allowed between characters in any input fields.
If space is allowed, then during read data from file to list will arise exception. 
Due to split separator space has been in use.

Note : Simple validations. Not covered all the cases. 

"""
#name 
def validate_name(name):
    def alpha_score(name):
        has_alpha=False
        for char in name:
            if char.isalpha() or char=='_':
                if char.isalpha():
                    has_alpha=True
            else:
                return False
        return has_alpha and True

    if(len(name)>0 and alpha_score(name)): #check name is not empty and only contains (A-Z,a-z) [at least one] and/or (_)
        return True
    else:
        common_function.show_msg("Invalid input.")
        print("# 1.At least one alphabetic character should present. (A-Z,a-z)")
        print("# 2.Only Alphabetic character (A-Z,a-z) and Special character (_) allowed.")
        print("# 3.For example : Md_Shuhan_Miah")
        return False

#phone number 
def validate_phn_num(contacts,phone_number):
    
    matched_index=common_function.get_matched_index(contacts,phone_number) #search 

    #duplicate number checking
    if matched_index!=-1 :
        common_function.show_msg("Number already present. Enter a unique number.")
        return False
    elif phone_number.isdigit(): #check phone number only contains digit or not 
        return True
    else:
        common_function.show_msg("Invalid input.")
        print("# 1.At least one digit should present.")
        print("# 2.Only digit allowed. (0-9)")
        print("# 3.For example : 0123456789")
        return False

#email  
def validate_email(email):
    if len(email)==0 or (' ' in email): #check email is empty or contains spaces  
        common_function.show_msg("Invalid input.")
        print("# 1.At least one character should present.")
        print("# 2.Space not allowed.")
        print("# 3.For example : shuhan1272@gmail.com")
        return False
    else:
        return True

#address
def validate_address(address):
    if len(address)==0 or (' ' in address): #check address is empty or contains spaces
        common_function.show_msg("Invalid input.")
        print("# 1.At least one character should present.")
        print("# 2.Space not allowed.")
        print("# 3.For example : Habiganj,Sylhet")
        return False
    else:
        return True

    

    


