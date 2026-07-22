import sys,os
print("MiniShell V1.O")
print("Type 'help' for commands: ")
cmdlist = []
def touch(command):
    folder = command[6: ]
    try:
        file = open(folder, "a")
        file.close()
    except FileExistsError:
        print("File Already exist")
    except PermissionError:
        print("Permission denied")
def Remove(command):
    file = command[3:]
    try:
        if os.path.isdir(file):
            print("It's a directory not a file.")
        elif os.path.isfile(file):
            os.remove(file)
            print("File deleted succesfully. ")
    except PermissionError:
        print("Permission Denied!")
def  cat(command):
    try:
        file = command[4:]
        with open(file, "r")as file:
            data = file.read()
        print(data)
    except FileNotFoundError:
        print("File doesn't exist")
    except IsADirectoryError:
        print("It is a directory not a file.")
    except PermissionError:
        print("Access denied to this file")
    except UnicodeDecodeError:
        print("Can not display this file, It is not a text file.")
while True:
    command = input(f"{os.getcwd()}\\MiniShell:>")
    cmdlist.append(command)
    if command == 'exit':
        sys.exit()
    elif(command == 'cls' or command == 'clear'):
        os.system("cls")
    elif command.lower() == 'history':
        for i,cmd in enumerate(cmdlist, start = 1):
            print(f"{i}.{cmd}")
    elif command == 'pwd':
        print(os.getcwd())
    elif command == 'ls':
        folders = os.listdir()
        for i in folders:
            print(i)
    elif command.startswith("cd "):
        folder = command[3: ]
        try:
            os.chdir(folder)
            print(os.getcwd())
        except FileNotFoundError:
            print("No Directory avalaible")
        except NotADirectoryError:
            print("Path is a file, not a directory.")
    elif command.startswith("mkdir "):
        folder = command[6: ]
        if os.path.exists(folder):
            print("Directory already exist. ")
        else:
           os.mkdir(folder)
    elif command.startswith("rmdir "): 
        folder = command[6: ]
        try: 
            os.rmdir(folder)
            print("Directory removed Successfully.")
        except FileNotFoundError:
            print("Directory doesn't exist")
        except OSError:
            print("Directory is not empty. ")
    elif command.startswith("touch "):
        touch(command)
    elif command.startswith("rm "):
        Remove(command)
    elif command.startswith("cat "):
        cat(command)
        
    else:
        print("Unknown command! ")