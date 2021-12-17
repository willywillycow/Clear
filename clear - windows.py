####################clear####################
###############import modules###############
##########sys##########
import sys as s
##########os##########
import os as o
##########pyperclip##########
import pyperclip as pcl
##########tkinter##########
import tkinter as tk
##########file dialog##########
import tkinter.filedialog as fd
###############output###############
##########set ups##########
#####variables#####
actions = ["clear","quit","help","show clip","show directory","rename","hide item","show item","show all hidden items","hide all hidden items","clear clip","clear item","clear directory","clear index","clear extension"]
action = None
path = None
item = None
directory = None
located = None
index = None
name = None
extension = None
target = None
mode = None
dialog = None
option = None
confirm = None
#####functions#####
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
    action = input("action: ")
#####detection#####
    if action in actions:
#####clear#####
        if action == "clear":
            print("Thanks for using clear!\nClear, created by Liansheng.\nOfficial website: https://sites.google/com/view/liansheng")
#####quit#####
        if action == "quit":
            action = None
            path = None
            item = None
            directory = None
            located = None
            index = None
            name = None
            extension = None
            target = None
            mode = None
            dialog = None
            option = None
            confirm = None
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
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
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
            if mode == "dialog":
                dialog = tk.Tk()
                dialog.geometry("0x0+0+0")
                dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                dialog.withdraw()
                path = fd.askdirectory(title = "select target directory")
                dialog.destroy()
                if path != "":
                    if o.path.exists(path):
                        if o.path.isfile(path):
                            print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                        elif o.path.isdir(path):
                            print("------------------------------"+o.path.basename(path)+"------------------------------")
                            for item in o.listdir(path):
                                print(item)
                            print("------------------------------end------------------------------")
                    else:
                        print("Sorry, we could not find the path you have given, please check if path target still exists.")
                elif path == "":
                    print("Successfully cancelled.")
            else:
                print("Sorry, invalid mode.")
#####rename#####
        if action == "rename":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    name = input("name: ")
                    confirm = input("confirm to proceed?\n(yes/no): ")
                    if confirm == "yes":
                        o.rename(path, o.path.dirname(path) + "/" + name)
                        print("Cleared.")
                    elif confirm == "no":
                        print("Successfully cancelled.")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode== "dialog":
                    option = input("directory or file: ")
                    if option == "file":
                        dialog = tk.Tk()
                        dialog.geometry("0x0+0+0")
                        dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                        dialog.withdraw()
                        path = fd.askopenfilename(title = "select target file")
                        dialog.destroy()
                        if path != "":
                            if o.path.exists(path):
                                name = input("name: ")
                                print("path: " + path)
                                print("location: " + o.path.dirname(path))
                                print("name: " + o.path.basename(o.path.splitext(path)[0]))
                                print("extension: " + o.path.splitext(path)[1])
                                print("new name: " + name)
                                confirm = input("confirm to proceed?\n(yes/no): ")
                                if confirm == "yes":
                                    o.rename(path, o.path.dirname(path) + "/" + name)
                                    print("Cleared.")
                                elif confirm == "no":
                                    print("Successfully cancelled.")
                            else:
                                print("Sorry, we could not find the path you have given, please check if path target still exists.")
                        elif path == "":
                            print("Successfully cancelled.")
                    elif option == "directory":
                        dialog = tk.Tk()
                        dialog.geometry("0x0+0+0")
                        dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                        dialog.withdraw()
                        path = fd.askdirectory(title = "select target directory")
                        dialog.destroy()
                        if path != "":
                            if o.path.exists(path):
                                name = input("name: ")
                                print("path: " + path)
                                print("location: " + o.path.dirname(path))
                                print("name: " + o.path.basename(o.path.splitext(path)[0]))
                                print("extension: *-DIRECTORY-*")
                                print("new name: " + name)
                                confirm = input("confirm to proceed?\n(yes/no): ")
                                if confirm == "yes":
                                    o.rename(path, o.path.dirname(path) + "/" + name)
                                    print("Cleared.")
                                elif confirm == "no":
                                    print("Successfully cancelled.")
                            else:
                                print("Sorry, we could not find the path you have given, please check if path target still exists.")
                        elif path == "":
                            print("Successfully cancelled.")
                    else:
                        print("Sorry. invalid option.")
            else:
                print("Sorry, invalid mode.")
#####hide item#####
        if action == "hide item":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("path: " + path)
                        print("location: " + o.path.dirname(path))
                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                        print("extension: " + o.path.splitext(path)[1])
                    elif o.path.isdir(path):
                        print("path: " + path)
                        print("location: " + o.path.dirname(path))
                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                        print("extension: *-DIRECTORY-*")
                    confirm = input("confirm to proceed?\n(yes/no): ")
                    if confirm == "yes":
                        o.system("attrib +s +h " + path)
                        print("Cleared.")
                    elif confirm == "no":
                        print("Successfully cancelled.")
                    else:
                        print("Sorry. invalid option.")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode == "dialog":
                option = input("directory or file: ")
                if option == "file": 
                    dialog = tk.Tk()
                    dialog.geometry("0x0+0+0")
                    dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                    dialog.withdraw()
                    path = fd.askopenfilename(title = "select target file")
                    dialog.destroy()
                    if path != "":
                        if o.path.isfile(path):
                            print("path: " + path)
                            print("location: " + o.path.dirname(path))
                            print("name: " + o.path.basename(o.path.splitext(path)[0]))
                            print("extension: " + o.path.splitext(path)[1])
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                if o.path.exists(path):
                                    if o.path.isfile(path):
                                        o.system("attrib +s +h " + path)
                                        print("Cleared.")
                                    elif o.path.isdir(path):
                                        print("Sorry, the file you chosed cannot be reconized by us, please check the file.")
                                else:
                                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                            else:
                                print("Sorry. invalid option.")
                        elif o.path.isdir(path):
                            print("Sorry, the file you chosed cannot be reconized by us, please check the file.")
                    elif path == "":
                        print("Successfully cancelled.")
                elif option == "directory": 
                    dialog = tk.Tk()
                    dialog.geometry("0x0+0+0")
                    dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                    dialog.withdraw()
                    path = fd.askdirectory(title = "select target directory")
                    dialog.destroy()
                    if path != "":
                        if o.path.isdir(path):
                            print("path: " + path)
                            print("location: " + o.path.dirname(path))
                            print("name: " + o.path.basename(o.path.splitext(path)[0]))
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                if o.path.exists(path):
                                    if o.path.isfile(path):
                                        print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                                    elif o.path.isdir(path):
                                        o.system("attrib +s +h " + path)
                                else:
                                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                            else:
                                print("Sorry. invalid option.")
                        elif o.path.isfile(path):
                            print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                    elif path == "":
                        print("Successfully cancelled.")
            else:
                print("Sorry, invalid mode.")
#####show item#####
        if action == "show item":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("path: " + path)
                        print("location: " + o.path.dirname(path))
                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                        print("extension: " + o.path.splitext(path)[1])
                    elif o.path.isdir(path):
                        print("path: " + path)
                        print("location: " + o.path.dirname(path))
                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                        print("extension: *-DIRECTORY-*")
                    confirm = input("confirm to proceed?\n(yes/no): ")
                    if confirm == "yes":
                        o.system("attrib -s -h " + path)
                        print("Cleared.")
                    elif confirm == "no":
                        print("Successfully cancelled.")
                    else:
                        print("Sorry. invalid option.")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode == "dialog":
                option = input("directory or file: ")
                if option == "file":
                    o.system("attrib -s -h -r /s /d")
                    dialog = tk.Tk()
                    dialog.geometry("0x0+0+0")
                    dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                    dialog.withdraw()
                    path = fd.askopenfilename(title = "select target file")
                    dialog.destroy()
                    o.system("attrib +s +h +r /s /d")
                    if path != "":
                        if o.path.isfile(path):
                            print("path: " + path)
                            print("location: " + o.path.dirname(path))
                            print("name: " + o.path.basename(o.path.splitext(path)[0]))
                            print("extension: " + o.path.splitext(path)[1])
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                if o.path.exists(path):
                                    if o.path.isfile(path):
                                        o.system("attrib -s -h " + path)
                                        print("Cleared.")
                                    elif o.path.isdir(path):
                                        print("Sorry, the file you chosed cannot be reconized by us, please check the file.")
                                else:
                                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                            else:
                                print("Sorry. invalid option.")
                        elif o.path.isdir(path):
                            print("Sorry, the file you chosed cannot be reconized by us, please check the file.")
                    elif path == "":
                        print("Successfully cancelled.")
                elif option == "directory":
                    o.system("attrib -s -h -r /s /d")
                    dialog = tk.Tk()
                    dialog.geometry("0x0+0+0")
                    dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                    dialog.withdraw()
                    path = fd.askdirectory(title = "select target directory")
                    dialog.destroy()
                    o.system("attrib +s +h +r /s /d")
                    if path != "":
                        if o.path.isdir(path):
                            print("path: " + path)
                            print("location: " + o.path.dirname(path))
                            print("name: " + o.path.basename(o.path.splitext(path)[0]))
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                if o.path.exists(path):
                                    if o.path.isfile(path):
                                        print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                                    elif o.path.isdir(path):
                                        o.system("attrib -s -h " + path)
                                else:
                                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                            else:
                                print("Sorry. invalid option.")
                        elif o.path.isfile(path):
                            print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                    elif path == "":
                        print("Successfully cancelled.")
            else:
                print("Sorry, invalid mode.")
#####show all hidden items#####
        if action == "show all hidden items":
            confirm = input("confirm to proceed?\n(yes/no): ")
            if confirm == "yes":
                o.system("attrib -s -h -r /s /d")
                print("Cleared.")
            elif confirm == "no":
                print("Successfully cancelled.")
            else:
                print("Sorry. invalid option.")
#####hide all hidden items#####
        if action == "hide all hidden items":
            confirm = input("confirm to proceed?\n(yes/no): ")
            if confirm == "yes":
                o.system("attrib +s +h +r /s /d")
                print("Cleared.")
            elif confirm == "no":
                print("Successfully cancelled.")
            else:
                print("Sorry. invalid option.")
#####clear clip#####
        if action == "clear clip":
            print("clip: " + pcl.paste())
            confirm = input("confirm to proceed?\n(yes/no): ")
            if confirm == "yes":
                pcl.copy("")
                print("Cleared.")
            elif confirm == "no":
                print("Successfully cancelled.")
            else:
                print("Sorry. invalid option.")
#####clear item#####
        if action == "clear item":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("path: " + path)
                        print("location: " + o.path.dirname(path))
                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                        print("extension: " + o.path.splitext(path)[1])
                    elif o.path.isdir(path):
                        print("path: " + path)
                        print("location: " + o.path.dirname(path))
                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                        print("extension: *-DIRECTORY-*")
                    confirm = input("confirm to proceed?\n(yes/no): ")
                    if confirm == "yes":
                        if o.path.isfile(path):
                            o.remove(path)
                        elif o.path.isdir(path):
                            empty(path)
                        o.rmdir(path)
                        print("Cleared.")
                    elif confirm == "no":
                        print("Successfully cancelled.")
                    else:
                        print("Sorry. invalid option.")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode == "dialog":
                option = input("directory or file: ")
                if option == "file":
                    dialog = tk.Tk()
                    dialog.geometry("0x0+0+0")
                    dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                    dialog.withdraw()
                    path = fd.askopenfilename(title = "select target file")
                    dialog.destroy()
                    if path != "":
                        if o.path.isfile(path):
                            print("path: " + path)
                            print("location: " + o.path.dirname(path))
                            print("name: " + o.path.basename(o.path.splitext(path)[0]))
                            print("extension: " + o.path.splitext(path)[1])
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                if o.path.exists(path):
                                    if o.path.isfile(path):
                                        o.remove(path)
                                        print("Cleared.")
                                    elif o.path.isdir(path):
                                        print("Sorry, the file you chosed cannot be reconized by us, please check the file.")
                                else:
                                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                        elif o.path.isdir(path):
                            print("Sorry, the file you chosed cannot be reconized by us, please check the file.")
                    elif path == "":
                        print("Successfully cancelled.")
                elif option == "directory":
                    dialog = tk.Tk()
                    dialog.geometry("0x0+0+0")
                    dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                    dialog.withdraw()
                    path = fd.askdirectory(title = "select target directory")
                    dialog.destroy()
                    if path != "":
                        if o.path.isdir(path):
                            print("path: " + path)
                            print("location: " + o.path.dirname(path))
                            print("name: " + o.path.basename(o.path.splitext(path)[0]))
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                if o.path.exists(path):
                                    if o.path.isfile(path):
                                        print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                                    elif o.path.isdir(path):
                                        empty(path)
                                        o.rmdir(path)
                                else:
                                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                        elif o.path.isfile(path):
                            print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                    elif path == "":
                        print("Successfully cancelled.")
            else:
                print("Sorry, invalid mode.")
#####clear directory#####
        if action == "clear directory":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("Sorry, you need a directory in order to use this command, not a file.")
                    elif o.path.isdir(path):
                        directory = o.listdir(path)
                        print("path: " + path)
                        print("location: " + path)
                        print("name: " + o.path.basename(path))
                        print("items: " + str(len(o.listdir(path))))
                        confirm = input("confirm to proceed?\n(yes/no): ")
                        if confirm == "yes":
                            empty(path)
                            print("Cleared.")
                        elif confirm == "no":
                            print("Successfully cancelled.")
                        else:
                            print("Sorry. invalid option.")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode == "dialog":
                dialog = tk.Tk()
                dialog.geometry("0x0+0+0")
                dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                dialog.withdraw()
                path = fd.askdirectory(title = "select target directory")
                dialog.destroy()
                if path != "":
                    if o.path.exists(path):
                        if o.path.isfile(path):
                            print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                        elif o.path.isdir(path):
                            directory = o.listdir(path)
                            print("path: " + path)
                            print("location: " + path)
                            print("name: " + o.path.basename(path))
                            print("items: " + str(len(o.listdir(path))))
                            confirm = input("confirm to proceed?\n(yes/no): ")
                            if confirm == "yes":
                                empty(path)
                                print("Cleared.")
                            elif confirm == "no":
                                print("Successfully cancelled.")
                            else:
                                print("Sorry. invalid option.")
                elif path == "":
                    print("Successfully cancelled.")
                else:
                    print("Sorry, we could not find the path you have given, please check if path target still exists.")
            else:
                print("Sorry, invalid mode.")
#####clear index#####
        if action == "clear index":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("Sorry, you need a directory in order to use this command, not a file.")
                    elif o.path.isdir(path):
                        index = input("index: ")
                        try:
                            index = int(index) - 1
                            directory = o.listdir(path)
                            if index in range(len(o.listdir(path))):
                                if o.path.isfile(path+ "/" +directory[index]):
                                    print("path: " + path+ "/" + directory[index])
                                    print("location: " + path)
                                    print("name: " + o.path.basename(o.path.splitext(path)[0]))
                                    print("extension: " + o.path.splitext(path+ "/" +directory[index])[1])
                                elif o.path.isdir(path+ "/" +directory[index]):
                                    print("path: " + path+ "/" + directory[index])
                                    print("location: " + path)
                                    print("name: " + o.path.basename(path))
                                    print("extension: *-DIRECTORY-*")
                                confirm = input("confirm to proceed?\n(yes/no): ")
                                if confirm == "yes":
                                    directory = o.listdir(path)
                                    if o.path.isfile(path+ "/" +directory[index]):
                                        o.remove(path+ "/" +directory[index])
                                    elif o.path.isdir(path+ "/" +directory[index]):
                                        empty(path+ "/" +directory[index])
                                    o.rmdir(path+ "/" +directory[index])
                                    print("Cleared.")
                                elif confirm == "no":
                                    print("Successfully cancelled.")
                                else:
                                    print("Sorry. invalid option.")
                            else:
                                print("Sorry, your index is out of range.")
                        except ValueError:
                            print("Sorry, your input is invalid, please input integers.")
                else:
                    print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode == "dialog":
                dialog = tk.Tk()
                dialog.geometry("0x0+0+0")
                dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                dialog.withdraw()
                path = fd.askdirectory(title = "select target directory")
                dialog.destroy()
                if path != "":
                    if o.path.exists(path):
                        if o.path.isfile(path):
                            print("Sorry, the directory you chosed cannot be reconized by us, please check the directory.")
                        elif o.path.isdir(path):
                            index = input("index: ")
                            try:
                                index = int(index) - 1
                                directory = o.listdir(path)
                                if index in range(len(o.listdir(path))):
                                    if o.path.isfile(path+ "/" +directory[index]):
                                        print("path: " + path+ "/" + directory[index])
                                        print("location: " + path)
                                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                                        print("extension: " + o.path.splitext(path+ "/" +directory[index])[1])
                                    elif o.path.isdir(path+ "/" +directory[index]):
                                        print("path: " + path+ "/" + directory[index])
                                        print("location: " + path)
                                        print("name: " + o.path.basename(o.path.splitext(path)[0]))
                                        print("extension: *-DIRECTORY-*")
                                    confirm = input("confirm to proceed?\n(yes/no): ")
                                    if confirm == "yes":
                                        directory = o.listdir(path)
                                        if o.path.isfile(path+ "/" +directory[index]):
                                            o.remove(path+ "/" +directory[index])
                                        elif o.path.isdir(path+ "/" +directory[index]):
                                            empty(path+ "/" +directory[index])
                                        o.rmdir(path+ "/" +directory[index])
                                        print("Cleared.")
                                    elif confirm == "no":
                                        print("Successfully cancelled.")
                                    else:
                                        print("Sorry. invalid option.")
                                else:
                                    print("Sorry, your index is out of range.")
                            except ValueError:
                                print("Sorry, your input is invalid, please input integers.")
                    else:
                        print("Sorry, we could not find the path you have given, please check if path target still exists.")
                elif path == "":
                    print("Successfully cancelled.")
            else:
                print("Sorry, invalid mode.")
#####clear extension#####
        if action == "clear extension":
            mode = input("choose mode.\n(manual/dialog): ")
            if mode == "manual":
                path = input("path: ")
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("Sorry, you need a directory in order to use this command, not a file.")
                    elif o.path.isdir(path):
                        target = input("target extension: ")
                        directory = o.listdir(path)
                        print("path: " + path)
                        print("location: " + path)
                        print("name: " + o.path.basename(path))
                        print("items: " + str(len(o.listdir(path))))
                        confirm = input("confirm to proceed?\n(yes/no): ")
                        if confirm == "yes":
                            if target == "":
                                for item in directory:
                                    name, extension = o.path.splitext(item)
                                    if extension == target and not os.isdir(item):
                                        o.remove(path+"/"+item)
                            else:
                                if target == "*-DIRECTORY-*":
                                    for item in directory:
                                        if o.path.isdir(path+"/"+item):
                                            empty(path+"/"+item)
                                            o.rmdir(path+"/"+item)
                                else:
                                    for item in directory:
                                        name, extension = o.path.splitext(item)
                                        if extension == target:
                                            o.remove(path+"/"+item)
                                print("Cleared.")
                        elif confirm == "no":
                            print("Successfully cancelled.")
                        else:
                            print("Sorry. invalid option.")
                    else:
                        print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            elif mode == "dialog":
                dialog = tk.Tk()
                dialog.geometry("0x0+0+0")
                dialog.title("O0-#!#!#!#-FILE DIALOG-#!#!#!#-0O")
                dialog.withdraw()
                path = fd.askdirectory(title = "select target directory")
                dialog.destroy()
                if o.path.exists(path):
                    if o.path.isfile(path):
                        print("Sorry, you need a directory in order to use this command, not a file.")
                    elif o.path.isdir(path):
                        target = input("target extension: ")
                        directory = o.listdir(path)
                        print("path: " + path)
                        print("location: " + path)
                        print("name: " + o.path.basename(path))
                        print("items: " + str(len(o.listdir(path))))
                        confirm = input("confirm to proceed?\n(yes/no): ")
                        if confirm == "yes":
                            if target == "":
                                for item in directory:
                                    name, extension = o.path.splitext(item)
                                    if extension == target and not os.isdir(item):
                                        o.remove(path+"/"+item)
                            else:
                                if target == "*-DIRECTORY-*":
                                    for item in directory:
                                        if o.path.isdir(path+"/"+item):
                                            empty(path+"/"+item)
                                            o.rmdir(path+"/"+item)
                                else:
                                    for item in directory:
                                        name, extension = o.path.splitext(item)
                                        if extension == target:
                                            o.remove(path+"/"+item)
                                print("Cleared.")
                        elif confirm == "no":
                            print("Successfully cancelled.")
                        else:
                            print("Sorry. invalid option.")
                    else:
                        print("Sorry, we could not find the path you have given, please check if you have written it correctly.")
            else:
                print("Sorry, invalid mode.")
#####detection#####
    elif action == "":
        print("Sorry, please enter existing commands and not empty.")
    else:
        print("Sorry, we could not find your command, please check if you have spelled the command correctly.")
#####clear data#####
    action = None
    path = None
    item = None
    directory = None
    located = None
    index = None
    name = None
    extension = None
    target = None
    mode = None
    dialog = None
    option = None
    confirm = None
####################end####################
