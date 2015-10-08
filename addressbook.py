#-----------------------------------------------------------
# Name      :       addressbook.py
# Purpose   :       Phone Book / Address Book
#
# Author    :       Aswathy
#
# Created   :       8-October-2015
# Copyright :       (c) 2015 by Aswathy
# Licence   :       Linux licence
#------------------------------------------------------------

import pickle
import os
class Contact:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        
    def __str__(self):
        a = "\n----------------------------------------\n| Name   : | {0}\n| E-Mail : | {1}\n| Phone  : | {2}\n ----------------------------------------\n>".format(self.name,self.email,self.phone)
        return a
    def change_name(self,name):
        self.name=name
        
    def change_email(self,email):
        self.email=email
        
    def change_phone(self,phone):
        self.phone=phone
        
def add_contact():
    address_book_file=open("address_book_file","r")

    is_file_empty=os.path.getsize("address_book_file")==0

    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
    else:
        list_contacts=[]
    try:
        contact=get_contact_info_from_user()
        address_book_file=open("address_book_file","w")
        list_contacts.append(contact)
        pickle.dump(list_contacts,address_book_file)
        print "----------------------------"
        print "Contact Added !!! "
    except KeyboardInterrupt:
        print "----------------------------"
        print "Contact Not Added"
    except EOFError:
        print "----------------------------"
        print "Contact Not Added"
    finally:
        address_book_file.close()
    
def get_contact_info_from_user():
    try:
        print "----------------------------"
        contact_name=raw_input("Enter Contact Name : ")
        print "----------------------------"
        contact_email=raw_input("Enter Contact Email : ")
        print "----------------------------"
        contact_phone=raw_input("Enter Contact Phone Number : ")
        contact=Contact(contact_name,contact_email,contact_phone)
        return contact
    except EOFError as e:
        #print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e
    
def display_contacts():
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            print each_contact
    else:
        print "----------------------------"
        print "No Contacts in Address Book"
        return
    address_book_file.close()
    
def search_contact():
    #search_name=raw_input("Enter the name\n")
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        print "----------------------------"
        search_name=raw_input("Enter The Name : ")
        is_contact_found=False
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            contact_name=each_contact.name
            search_name=search_name.lower()
            contact_name=contact_name.lower()
            if(contact_name==search_name):
                print each_contact
                is_contact_found=True
                break
        if not is_contact_found:
            print "----------------------------"
            print "No Contact Found The Search Name"
    else:
        print "----------------------------"
        print "Address Book empty. No Contact to Search"
    address_book_file.close()

def delete_contact():
    #name=raw_input("Enter the name to be deleted\n")
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        print "----------------------------"
        name=raw_input("Enter the Name to be Deleted : ")
        list_contacts=pickle.load(address_book_file)
        is_contact_deleted=False
        for i in range(0,len(list_contacts)):
            each_contact=list_contacts[i]
            if each_contact.name==name:
                del list_contacts[i]
                is_contact_deleted=True
                print "----------------------------"
                print "Contact Deleted !!!"
                address_book_file=open("address_book_file","w")
                if(len(list_contacts)==0):
                    address_book_file.write("")
                else:
                    pickle.dump(list_contacts,address_book_file)
                break
        if not is_contact_deleted:
            print "----------------------------"
            print "Contact With This Name Not Found"
            
    else:
        print "----------------------------"
        print "Address Book Empty. No Contact To Delete"
    address_book_file.close()
    
def modify_contact():
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        print "----------------------------"
        name=raw_input("Enter the Name of the Contact to be Modified : ")
        list_contacts=pickle.load(address_book_file)
        is_contact_modified=False
        for each_contact in list_contacts:
            if each_contact.name==name:
                do_modification(each_contact)
                address_book_file=open("address_book_file","w")
                pickle.dump(list_contacts,address_book_file)
                is_contact_modified=True
                print "----------------------------"
                print "Contact Modified"
                break
        if not is_contact_modified:
            print "Contact with this Name Not Found"
    else:
        print "----------------------------"
        print "Address Book Empty. No Contact to Delete"
    address_book_file.close()
    
def do_modification(contact):
    try:
        while True:

            print ("Enter the number of the Option you want:"+
                "\n----------------------------------------"+
                "\n| 1 | To Modify Number"+
                "\n| 2 | To Modify E-Mail"+
                "\n| 3 | To quit\n"+
                "----------------------------------------\n>")
            choice=raw_input()
            if(choice=="2"):
                print "----------------------------"
                new_email=raw_input("Enter New Email Address : ")
                contact.change_email(new_email)
                break
            elif(choice=="1"):
                print "----------------------------"
                new_phone=raw_input("Enter New Phone Number : ")
                contact.change_phone(new_phone)
                break
            else:
                print "----------------------------"
                print "Incorrect Choice !!!"
                break
    except EOFError:
        print "EOF Error occurred"
    except KeyboardInterrupt:
        print "KeyboardInterrupt occurred"

######################################################################################

###############################################################################

option =0
while True:
    print "---------------------------------------"
    option = raw_input("Enter the number of the Option you want:"+
                "\n----------------------------------------"+
                "\n| 1 | To Add Contact"+
                "\n| 2 | To print the Address book"
                "\n| 3 | To Delete Contact"+
                "\n| 4 | To Modify Contact"
                "\n| 5 | To Search Contact"
                "\n| 6 | To quit\n"+
                "----------------------------------------\n>")


    if option == '6':
        break
    elif(option=='1'):

        print "-------------"
        print "Add Contacts!\n-------------"
        add_contact()

    elif(option=='2'):

        print "----------------------------"
        print "Printing the Address book\n-----------------------"
        display_contacts()

    elif(option=='3'):

        print "----------------------------"
        print "Delete the Contact!\n-----------------------"
        delete_contact()

    elif(option=='4'):

        print "----------------------------"
        print "\nEdit the Contact!\n------------------\n"
        modify_contact()

    elif(option=='5'):

        print "----------------------------"
        print "\nSearch Contact!\n----------------------------"

        search_contact()
    else:
        print "----------------------------"
        print "Incorrect choice. Need to enter the choice again"



