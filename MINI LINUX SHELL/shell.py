import sys,os,shutil
SHELL_DIR = os.path.dirname(os.path.abspath(__file__))
history_path = os.path.join(SHELL_DIR, "history.txt")
help_path = os.path.join(SHELL_DIR, "help.txt")
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
def echo(command):
    try: 
        if ">>" in command:
            left, right = command.split(">>")
            data = left[5: ]
            file = right.strip()
            with open(file, "a")as file:
                file.write(data +"\n")
        elif ">" in command:
            left, right = command.split(">")
            data = left[5: ].strip()
            filename = right.strip()
            with open(filename, "w")as file:
                file.write(data)
        else:
            data = command[5: ]
            print(f"{data}")
    except FileExistsError:
        print("File Already exist.")
def move(command):
    try: 
        part = command.split()
        source = part[1]
        destination = part[2]
        os.rename(source, destination)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Access denied to move the file!")
    except FileExistsError:
        print("File already exist in the directory.")
    except OSError:
        print("Invalid destination path.")
def copy(command):
    try:
        part = command.split()
        source = part[1]
        destination = part[2]
        shutil.copy(source, destination)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Access denied to copy this file.")
    except IsADirectoryError:
        print("Choosen item is a directory. ")
    except shutil.SameFileError:
        print("Source & destination are the same file.")
    except OSError:
        print("Invalid path.")
def change_directory(command):
    try:
        if command == '~':
            home = os.path.expanduser("~")
            os.chdir(home)
            return
        os.chdir(command)
    except FileNotFoundError:
            print("No Directory avalaible")
    except NotADirectoryError:
            print("Path is a file, not a directory.")
while True:
    command = input(f"{os.getcwd()}\\MiniShell:>")
    cmdlist.append(command)
    with open(history_path,"a")as file:
        file.write(command + "\n")
    if command == 'exit':
        print("Exiting from Minishell.")
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
    elif command.startswith("cd"):
        part = command.split(maxsplit = 1)
        if len(part)>1:
            change_directory(part[1])
        else:
            home = os.path.expanduser("~")
            os.chdir(home)
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
    elif command.startswith("echo "):
        echo(command)
    elif command.startswith("mv "):
        move(command)
    elif command.startswith("cp "):
        copy(command)
    elif command.lower() == 'help':
        with open(help_path, "r")as file:
            data = file.read()
        print(data)
        
    else:
        print("Unknown command! ")