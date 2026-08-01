import os,sys
SHELL_DIR = os.path.dirname(os.path.abspath(__file__))
history_path = os.path.join(SHELL_DIR, "history.txt")
help_path = os.path.join(SHELL_DIR, "help.txt")
def grep_pipe(word, data):
    found = False
    required_line = []
    for line in data:
        if word in line:
            required_line.append(line)
            found = True
    if not found:
        print("No match found!") 
    for datas in required_line: 
        return datas  
def cat_pipe(command):
    part = command.split()
    cmd = part[0]
    file_names = part[1:]
    datas = []
    try:
        for file in file_names:
            with open(file, "r")as f:
                data = f.read()
            datas.append(data)
    except FileNotFoundError:
        print("File doesn't exist")
    except IsADirectoryError:
        print("It is a directory not a file.")
    except PermissionError:
        print("Access denied to this file")
    except UnicodeDecodeError:
        print("Can not display this file, It is not a text file.")
    return datas
