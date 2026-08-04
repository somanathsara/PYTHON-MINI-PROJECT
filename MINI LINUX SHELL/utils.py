import os,sys,commands
from colorama import Fore, init, Back
SHELL_DIR = os.path.dirname(os.path.abspath(__file__))
history_path = os.path.join(SHELL_DIR, "history.txt")
help_path = os.path.join(SHELL_DIR, "help.txt")
def grep_redirection(command):
    part = command.split(">")
    left = part[0].strip()
    right = part[1].strip()
    data = commands.grep(left)
    for line in data:
        with open (right, "a")as file:
            file.write(line)
def grep_pipe(args, data):
    found = False
    word = args[0]
    required_line = []
    for line in data:
        if word in line:
            required_line.append(line)
            found = True
    if not found:
        print("No match found!") 
    return required_line 
def cat_pipe(args, data):
    datas = []
    try:
        for file in args:
            with open(file, "r")as f:
                content = f.readlines()
            datas.extend(content)
    except FileNotFoundError:
        print("File doesn't exist")
    except IsADirectoryError:
        print("It is a directory not a file.")
    except PermissionError:
        print("Access denied to this file")
    except UnicodeDecodeError:
        print("Can not display this file, It is not a text file.")
    return datas
def head_pipe(args, data):
    req_data = data[:10]
    return req_data        
def tail_pipe(args, data):
    req_data = data[-10:]
    return req_data
def wc_pipe(args, data):
    print(len(data))
def sort_pipe(args, data):
    ...
def uniq_pipe(args, data):
    ...
def color(command):
    colors = {
                "red":Fore.RED,
                "green":Fore.GREEN,
                "blue":Fore.BLUE,
                "yellow":Fore.YELLOW,
                "white":Fore.WHITE,
                "reset":Fore.RESET,
                "cyan":Fore.CYAN,
                "magneta":Fore.MAGENTA
            }
    part = command.split()
    if part[1] in colors:
        cureent_color = colors[part[1]]
    else:
        print("Invalid color!")
    return cureent_color
    
    
