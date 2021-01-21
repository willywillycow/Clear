####################clear####################
###############import modules###############
##########sys##########
import sys as s
##########os##########
import os as o
##########pyperclip##########
import pyperclip as pcl
###############output###############
##########set ups##########
actions = ["clear","quit","help","show clip","show directory","rename","hide item","show item","show all hidden items","hide all hidden items","clear clip","clear item","clear directory","clear index","clear extension"]
action = False
path = False
item = False
directory = False
located = False
index = False
name = False
extension = False
target = False
def empty(path):
    for item in o.listdir(path):
        if o.path.isfile(path+"/"+item):
            o.remove(path+"/"+item)
        elif o.path.isdir(path+"/"+item):
            empty(path+"/"+item)
            o.rmdir(path+"/"+item)
##########prompt##########
print("Thanks for using clear!\nClear, created by Liansheng.\nOfficial website: https://sites.google.com/view/liansheng")
##########action##########
while True:
#####input#####
    action = input("Action: ")
#####detection#####
    if action in actions:
#####clear#####
        if action == "clear":
            print("Thanks for using clear!\nClear, created by Liansheng.\nOfficial website: https://sites.google/com/view/liansheng")
#####quit#####
        if action == "quit":
            action = False
            path = False
            item = False
            directory = False
            located = False
            index = False
            name = False
            extension = False
            target = False
            s.exit()
            o._quit()
            quit()
#####help#####
        if action == "help":
            print("------------------------------help------------------------------")
            for item in actions:
                print(item)
            print("\033[1m directory \033[0m equals to \033[1m *-DIRECTORY-* \033[0m")
            print("------------------------------end------------------------------")
#####show clip#####
        if action == "show clip":
            print("---------------clipboard---------------")
            print(pcl.paste())
            print("---------------end---------------")
#####show directory#####
        if action == "show directory":
            path = input("path: ")
            if o.path.exists(path):
                if o.path.isfile(path):
                    print("Sorry, you need a directory in order to use this command, not a file.")
                elif o.path.isdir(path):
                    print("------------------------------"+o.path.basename(path)+"------------------------------")
                    for item in o.listdir(path):
                        print(item)
                    print("------------------------------end------------------------------")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####rename#####
        if action == "rename":
            path = input("path: ")
            if o.path.exists(path):
                name = input("name: ")
                o.rename(path, o.path.dirname(path)+"/"+name)
                print("Cleared.")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####hide item#####
        if action == "hide item":
            path = input("path: ")
            if o.path.exists(path):
                o.system("attrib +s +h "+path)
                print("Cleared.")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####show item#####
        if action == "show item":
            path = input("path: ")
            if o.path.exists(path):
                o.system("attrib -s -h "+path)
                print("Cleared")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####show all hidden items#####
        if action == "show all hidden items":
            o.system("attrib -s -h -r /s /d")
            print("Cleared.")
#####hide all hidden items#####
        if action == "hide all hidden items":
            o.system("attrib +s +h +r /s /d")
            print("Cleared.")
#####clear clip#####
        if action == "clear clip":
            pcl.copy("")
            print("Cleared.")
#####clear item#####
        if action == "clear item":
            path = input("path: ")
            if o.path.exists(path):
                if o.path.isfile(path):
                    o.remove(path)
                elif o.path.isdir(path):
                    empty(path)
                    o.rmdir(path)
                print("Cleared.")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####clear directory#####
        if action == "clear directory":
            path = input("path: ")
            if o.path.exists(path):
                if o.path.isfile(path):
                    print("Sorry, you need a directory in order to use this command, not a file.")
                elif o.path.isdir(path):
                    empty(path)
                    print("Cleared.")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####clear index#####
        if action == "clear index":
            path = input("path: ")
            if o.path.exists(path):
                if o.path.isfile(path):
                    print("Sorry, you need a directory in order to use this command, not a file.")
                elif o.path.isdir(path):
                    index = input("index: ")
                    try:
                        index = int(index)
                        if o.path.isdir(path):
                            directory = o.listdir(path)
                            if o.path.isfile(path+"/"+directory[index]):
                                o.remove(path+"/"+directory[index])
                            elif o.path.isdir(path+"/"+directory[index]):
                                empty(path+"/"+directory[index])
                                o.rmdir(path+"/"+directory[index])
                            print("Cleared.")
                        else:
                            print("Sorry, your index is out of range.")
                    except ValueError:
                        print("Sorry, your input is invalid, please input integers.")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####clear extension#####
        if action == "clear extension":
            path = input("path: ")
            if o.path.exists(path):
                if o.path.isfile(path):
                    print("Sorry, you need a directory in order to use this command, not a file.")
                elif o.path.isdir(path):
                    target = input("target extension: ")
                    directory = o.listdir(path)
                    if target == "":
                        print("Sorry, you need you input a extension type, not empty. If you want to delete directory then please enter \033[1m *-DIRECTORY-*.")
                    else:
                        if target == "*-DIRECTORY-*":
                            for item in directory:
                                if o.path.isdir(path+"/"+item):
                                    empty(path+"/"+item)
                                    o.rmdir(path+"/"+item)
                        else:
                            for item in directory:
                                name, extension = o.path.splitext(item)
                                if extension.replace(".","") == target:
                                    print("test")
                                    o.remove(path+"/"+item)
                        print("Cleared.")
            else:
                print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
#####detection#####
    elif action == "":
        print("Sorry, please enter existing commands and not empty.")
    else:
        print("Sorry, we could not find your command, please check if you have spelled the command correctly.")
#####clear data#####
    action = False
    path = False
    item = False
    directory = False
    located = False
    index = False
    name = False
    extension = False
    target = False
####################end####################
