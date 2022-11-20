#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEMPLATE = "Day24_mail_merge/Input/Letters/starting_letter.txt"
NAMES_LIST = "Day24_mail_merge/Input/Names/invited_names.txt"
TARGET_FOLDER = "Day24_mail_merge/Output/ReadyToSend/"

def import_template(template_file):
    #read a template of a invitation
    with open(template_file, mode="r") as file:
        template = file.read()
    return template

def import_guests(guests_list):
    #import the names from a txt files and return the list with names
    invited = []
    with open(guests_list, mode="r") as guests:
        #read names from a guest list
        invited = guests.readlines()
        # remove "\n"
        for idx, inv in enumerate(invited):
            if "\n" in inv:
                inv_new = inv.replace("\n", "")
                invited[idx] = inv_new
    return invited

def merge_mail(target_folder, template, guest_list):
    #takes a template, replace [name] with name and save a txt in specific folder
    for name in guest_list:
        invitation = template.replace("[name]", name)
        filename = target_folder + "letter_for_" + name + ".txt"
        with open(filename, mode="w") as file:
            file.write(invitation)



template = import_template(TEMPLATE)
guest_list = import_guests(NAMES_LIST)
merge_mail(TARGET_FOLDER, template, guest_list)
