#============Import Statements==============
import time
import sys
import os
from os.path import expanduser
import getpass
import socket
import argparse
import fileinput

#==========Global Variables============
HOME = expanduser("~") # Generate log file in home directory
LOG_NAME = "CHANGELOG.txt" # Name of log file
HEADER_TEXT= "System Changelog" # in-text header
STARTING_LINE= 11 # Where each entry appends at (spacing)
CURRENT_TIME = time.strftime("%I:%M:%S")
CURRENT_DATE = time.strftime("%d/%m/%Y")


#=============Terminal Colors===================
SUCCESS = '\033[92m' #Light Green
FAIL = '\033[91m'    #Light Red
PROMPT = '\033[93m' #Light Yellow
COL_EXIT = '\033[0m' #Color Reset 

#===============Log Colors==================
TODO_COLOR = '\033[96m'  #Light Cyan
ADD_COLOR = '\033[92m'     #Light Green
REMOVE_COLOR = '\033[31m'  #Red
TIME_COLOR = '\033[93m' # Light Yellow


#================Functions==================

def log_generate(): #generates the initial log file

    os.chdir(HOME)
    if os.path.isfile(LOG_NAME):
        print("[x] {}{} already exists, aborting...{}".format(FAIL, LOG_NAME, COL_EXIT))
        sys.exit()
    else:
        print("[*] {}{} successfully created!{}".format(SUCCESS, LOG_NAME, COL_EXIT))
        textfile = open(LOG_NAME,"w+")
        banner_gen(textfile)
        sys.exit()

def log_delete(): # deletes log file
    os.chdir(HOME)
    try:
        user_prompt = input("[?] {}Are you sure you want to delete {}{}{}? (y or n){}: ".format(PROMPT, COL_EXIT, LOG_NAME, PROMPT, COL_EXIT))
        if user_prompt in ("y", "Y", "yes", "Yes"):
            os.remove(LOG_NAME)
            print("[*] {}{} successfully removed!{}".format(SUCCESS, LOG_NAME, COL_EXIT))        
            sys.exit()
        elif user_prompt in ("n", "N", "no", "No"):
            print("[x] {}Deletion aborted...{}".format(FAIL, COL_EXIT))
            sys.exit()
        else:
            print("[x] {}Not valid input, aborting...{}".format(FAIL, COL_EXIT))
    except FileNotFoundError:
        print("[x]{} No log file found, aborting...{}".format(FAIL, COL_EXIT) )
        sys.exit()    

def log_show():
    os.chdir(HOME)
    try:
        with open(LOG_NAME, 'r') as open_file:
            print(open_file.read(), end="")
            open_file.close()
    except FileNotFoundError:
            print("[x]{} No log file found, aborting...{}".format(FAIL, COL_EXIT) )
            sys.exit() 

def banner_gen(openfile): #generates the header of logfile

    username = getpass.getuser()
    hostname = socket.gethostname()
    openfile.write(
"""========================================================
[*] {}
[*] Generated by user '{}' on host '{}'
[*] Time Created: {}
[*] Date Created: {}
========================================================\n""".format(HEADER_TEXT, username, hostname, CURRENT_TIME, CURRENT_DATE))
    openfile.close()


def entry_create(): #creates an entry header
    os.chdir(HOME)
    try:
        f = open(LOG_NAME, "r")
    except FileNotFoundError:
        print("[x] {}{} does not exist, aborting...{}".format(FAIL, LOG_NAME, COL_EXIT))
        sys.exit()
    contents = f.readlines()
    f.close()
    contents.insert(STARTING_LINE, """\n\n[*] Entry On {}
 ========================\n""".format(CURRENT_DATE))

    f = open(LOG_NAME, "w")
    contents = "".join(contents)
    f.write(contents)
    print("[*] {}Entry Header Created.{}".format(SUCCESS, COL_EXIT))
    f.close
    sys.exit()


def event_add():
    os.chdir(HOME)
    try:
        f = open(LOG_NAME, "r")
    except FileNotFoundError:
        print("[x] {}{} does not exist, aborting...{}".format(FAIL, LOG_NAME, COL_EXIT))
        sys.exit()
    contents = f.readlines()
    f.close()
    user_prompt = input("{}Addition{}: ".format(PROMPT, COL_EXIT))    
    contents.insert(11, "{}[+] {}{}{}{}: {}\n".format(ADD_COLOR, COL_EXIT, TIME_COLOR,CURRENT_TIME,COL_EXIT, user_prompt))
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
        print("[x] {}{} does not exist, aborting...{}".format(FAIL, LOG_NAME, COL_EXIT))
        sys.exit()
    contents = f.readlines()
    f.close()
    user_prompt = input("{}Removal{}: ".format(PROMPT, COL_EXIT))    
    contents.insert(11, "{}[-] {}{}{}{}: {}\n".format(REMOVE_COLOR, COL_EXIT, TIME_COLOR, CURRENT_TIME, COL_EXIT, user_prompt))
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
        print("[x] {}{} does not exist, aborting...{}".format(FAIL, LOG_NAME, COL_EXIT))
        sys.exit()
    contents = f.readlines()
    f.close()
    user_prompt = input("{}Todo{}: ".format(PROMPT, COL_EXIT))    
    contents.insert(11, "{}[=] {}{}{}{}: {}\n".format(TODO_COLOR, COL_EXIT, TIME_COLOR, CURRENT_TIME, COL_EXIT,user_prompt))
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
    parser.add_argument("-s","--show", action="store_true", help="Show's the log file")    
    parser.add_argument("-c","--create", action="store_true", help='Creates an file banner')
    parser.add_argument("-a","--add", action="store_true", help="Addition tag")
    parser.add_argument("-r","--remove", action="store_true", help="Removal tag ")
    parser.add_argument("-t","--todo", action="store_true", help="Todo tag ")
    # parser.add_argument("-b","--backup", action="store_true", help="Creates a copy of logfile")
    # parser.add_argument("-e","--email", action="store_true", help="Emails changelog ")


    args = parser.parse_args()

    if args.generate:
        log_generate()
    elif args.create:
        entry_create()
    elif args.delete:
        log_delete()
    elif args.show:
        log_show()
    elif args.add:
        event_add()
    elif args.remove:
        event_remove()
    elif args.todo:
        event_todo()
    else:
        print("[*] {}Invalid argument, aborting...{}".format(FAIL, COL_EXIT))
        sys.exit()




if __name__ == "__main__":
    main()
