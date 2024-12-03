#display header   
def show_header(header):
    header ="* "+header+" *"
    print("*"*len(header),header,"*"*len(header),sep='\n')

#display output message   
def show_msg(message):
    header ="| "+message+" |"
    print("-"*len(header),header,"-"*len(header),sep='\n')

#function for getting matched index [Common function for search,remove and checking duplicate phone_number.]
def get_matched_index(contacts,phone_number):
    #searching 
    index,matched_index = -1,-1 #if no contact matched return -1 
    for contact in contacts:
        index+=1
        if contact['phone_number']==phone_number:
            matched_index=index
            break 
    return matched_index