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
        part = command.split(maxsplit = 2)
        source = part[1]
        destination = part[2]
        if os.path.isdir(destination):
            destination = os.path.join(destination,os.path.basename(source))
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
def tree(path,prefix = ""):
    data = os.listdir(path)
    for index,i in enumerate(data,start = 0):
        full_path =  os.path.join(path,i)
        if len(data) - 1 == index:
            new_prefix = prefix + "        "
        else:
            new_prefix = prefix + "|       "
        if len(data) - 1 == index:
            connector = "|_____"
        else:
            connector = "|-----"
        if i.startswith("."):
            continue
        print(prefix + connector + i)
        if os.path.isdir(full_path):
            tree(full_path,new_prefix)
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
def find(target):
    try:
        found = False
        for root, dirs, files in os.walk("G:\\"):
            for i  in files:
                if i == target:
                    print(os.path.join(root, i))
                    found = True
            for d in dirs:
                if d == target:
                    print(os.path.join(root, d))
                    found = True
        if not found:
            print("File not found")     
    except PermissionError:
        print("Access denied to see this files.")
def insensitive_grep(word, file):
    with open(file, "r")as file:
        data = file.readlines()
    for line in data:
        if word.lower() in line.lower():
            print(line,end = "")
    print("\n")
def count_grep(word, file):
    count_num = 0
    with open(file, "r")as file:
        data = file.readlines()
    for line in data:
        show = line.count(word)
        count_num += show
    print(count_num)
def linenum_grep(word, file):
    found = False
    with open(file, "r")as file:
        data = file.readlines()
    for index,line in enumerate(data,start = 1):
        if word in line:
            found = True
            print(f"{index} . {line}",end = "")
    print("\n")
    if not found:
        print("No line found contain this word.")  
def grep(command):
    part = command.split(maxsplit = 1)
    cmd = part[0]
    other = part[1]
    try:
        found = False
        if other.startswith("-"):
            new_part = other.split(maxsplit=2)
            option_flag = new_part[0]
            word = new_part[1]
            file = new_part[2]
            if option_flag == "-i":
                insensitive_grep(word, file)
            elif option_flag == '-c':
                count_grep(word, file)
            elif option_flag == '-n':
                linenum_grep(word, file)
        else:
            new_part = other.split()
            word =  new_part[0]
            file = new_part[1]
            with open(file, "r")as f:
                data = f.readlines()
            for line in data:
                if word in line:
                    found = True
                    print(line,end ="")
            print("\n")
            if not found:
                print("No match file found.")
    except FileNotFoundError:
        print("File not found")
def head(command):
    try:
        part = command.split()
        file = part[1]
        with open(file, "r")as file:
            data = file.readlines()
            if len(data)>10:
                for i in range(10):
                    print(data[i], end = "")
            else:
                for line in data:
                    print(line,end = "")
        print("\n")
    except FileNotFoundError:
        print("File not found")
    except IsADirectoryError:
        print("It's a directory.")
    except PermissionError:
        print("Access denied to this file.")
def tail(command):
    try:
        part = command.split()
        file = part[1]
        with open(file, "r")as file:
            data = file.readlines()
        if len(data)>10:
            reverse_data = data[-10:]
            for line in reverse_data:
                print(line,end ="")
        else:
            for line in data:
                print(line,end = "")
        print("\n")
    except FileNotFoundError:
        print("File doesn't Exist")
    except PermissionError:
        print("Access denied to this file.")
    except IsADirectoryError:
        print("It's a directory.")
while True:
    try: 
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
        elif command == 'tree':
            current_directory = os.getcwd()
            tree(current_directory,"")
        elif command.startswith("find "):
            path = command[5:]
            find(path)
        elif command.startswith("grep "):
            grep(command)
        elif command.startswith("head "):
            head(command)
        elif command.startswith("tail "):
            tail(command)
        else:
            print("Unknown command! ")
    except Exception as e:
        print(e)
