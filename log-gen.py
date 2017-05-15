#============Import Statements==============
import time
import sys
import os
from os.path import expanduser
import getpass
import socket
import argparse
import fileinput


#============Global Variables===============
HOME = expanduser("~") # Generate log file in home directory
LOG_NAME = "CHANGELOG.txt" # Name of log file
HEADER_TEXT= "System Changelog" # in-text header
STARTING_LINE= 11 # Where each entry appends at (spacing)


#================Functions==================

def log_generate(): #generates the initial log file

    os.chdir(HOME)
    if os.path.isfile(LOG_NAME):
        print("[*] {} already exists, aborting...".format(LOG_NAME))
        sys.exit()
    else:
        print("[*] {} successfully created!".format(LOG_NAME))
        textfile = open(LOG_NAME,"w+")
        banner_gen(textfile)
        sys.exit()

def log_delete(): # deletes log file
    os.chdir(HOME)
    try:
        os.remove(LOG_NAME)
        print("[*] {} successfully removed!".format(LOG_NAME))
        sys.exit()
    except FileNotFoundError:
        print("No log file was found, aborting...")
        sys.exit()    

def banner_gen(openfile): #generates the header of logfile

    username = getpass.getuser()
    hostname = socket.gethostname()
    currenttime = time.strftime("%I:%M:%S")
    currentdate = time.strftime("%d/%m/%Y")
    openfile.write(
"""========================================================
[*] {}
[*] Generated by user '{}' on host '{}'
[*] Time Created: {}
[*] Date Created: {}
========================================================\n""".format(HEADER_TEXT, username, hostname, currenttime, currentdate))
    openfile.close()


def entry_create(): #creates an entry header
    os.chdir(HOME)
    entrydate = time.strftime("%d/%m/%Y")

    try:
        f = open(LOG_NAME, "r")
    except FileNotFoundError:
        print("[*] {} does not exist, aborting...".format(LOG_NAME))
        sys.exit()
    contents = f.readlines()
    f.close()
    contents.insert(STARTING_LINE, """\n\n[*] Entry On {}
 ========================\n""".format(entrydate))

    f = open(LOG_NAME, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close
    sys.exit()


def event_add():
    os.chdir(HOME)
    try:
        f = open(LOG_NAME, "r")
    except FileNotFoundError:
        print("[*] {} does not exist, aborting...".format(LOG_NAME))
        sys.exit()
    contents = f.readlines()
    f.close()
    user_prompt = input("Addition: ")    
    contents.insert(11, "[+] {}\n".format(user_prompt))
    f = open(LOG_NAME, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close
    sys.exit()


def event_remove():
    os.chdir(HOME)
    try:
        f = open(LOG_NAME, "r")
    except FileNotFoundError:
        print("[*] {} does not exist, aborting...".format(LOG_NAME))
        sys.exit()
    contents = f.readlines()
    f.close()
    user_prompt = input("Removal: ")    
    contents.insert(11, "[-] {}\n".format(user_prompt))
    f = open(LOG_NAME, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close
    sys.exit()

def event_todo():
    os.chdir(HOME)
    try:
        f = open(LOG_NAME, "r")
    except FileNotFoundError:
        print("[*] {} does not exist, aborting...".format(LOG_NAME))
        sys.exit()
    contents = f.readlines()
    f.close()
    user_prompt = input("Todo: ")    
    contents.insert(11, "[=] {}\n".format(user_prompt))
    f = open(LOG_NAME, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close
    sys.exit()


#optional parsers need the action="store_true" parameter
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g","--generate", action="store_true", help='Generates logfile in HOME directory.')
    parser.add_argument("-d","--delete", action="store_true", help="Deletes logfile")
    parser.add_argument("-c","--create", action="store_true", help='Creates an file banner')
    parser.add_argument("-a","--add", action="store_true", help="Addition tag")
    parser.add_argument("-r","--remove", action="store_true", help="Removal tag ")
    parser.add_argument("-t","--todo", action="store_true", help="Todo tag ")




    args = parser.parse_args()

    if args.generate:
        log_generate()
    elif args.create:
        entry_create()
    elif args.delete:
        log_delete()
    elif args.add:
        event_add()
    elif args.remove:
        event_remove()
    elif args.todo:
        event_todo()
    else:
        print("[*] Invalid argument, aborting...")




if __name__ == "__main__":
    main()










# date = []
# entry_number = 0
# def entry_create(): #creates a daily entry
#     os.chdir(HOME)
#     entrydate = time.strftime("%d/%m/%Y")
#     if not entrydate in date:
#         date.append(entrydate)
#     elif entrydate in date[0]:
#         print("success")
#         sys.exit()
#     else:
#         date.append(entrydate)
#         sys.exit()




#entry_number = 1




 #   with open("CHANGELOG.txt","r") as textfile:
 #       lines = textfile.readlines()
 #       textfile.close()
 #   lines.insert(starting_line, "[*] Entry 1 on datehere")
 #   with open("CHANGELOG.txt","w") as write:
 #       write.writelines(





#                def entry_add():
#    entrydate = time.strftime("%d/%m/%Y")
#    date_check(entrydate)
#    pass




# def entry_print():
#     pass
# def todo_add():
#     pass
# def todo_del():
#     pass
# def todo_print():
#     pass

# if its current day and log alread made, skip, else, make new day



# def date_check(entrydate): #prevents multiple entry's from same date
#     date = []


#     if entrydate not in date:  #if list is empty
#         date.insert(0, entrydate)
#         print(1)
#     elif entrydate in date[0]: # if it's the same date
#         print("[*] Today's entry has already been created, aborting...")
#         print(2)
#         sys.exit()
#     else: #if another date, update to new date
#         del date[0]
#         date.append(0, entrydate)
#         print(3)

