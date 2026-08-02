import os
import shutil

SHELL_DIR = os.path.dirname(os.path.abspath(__file__))
history_path = os.path.join(SHELL_DIR, "history.txt")
help_path = os.path.join(SHELL_DIR, "help.txt")


def touch(command):
    folder = command[6:]
    try:
        file = open(folder, "a")
        file.close()
    except FileExistsError:
        print("File Already exist")
    except PermissionError:
        print("Permission denied")


def Remove(command):
    part = command.split()
    file_name = part[1:]
    try:
        for file in file_name:
            if os.path.isdir(file):
                print("It's a directory not a file.")
            elif os.path.isfile(file):
                os.remove(file)
                print("File deleted succesfully. ")
    except PermissionError:
        print("Permission Denied!")
    except FileNotFoundError:
        print("File doesn't exist")


def cat(command):
    try:
        part = command.split()
        file_names = part[1:]
        for file in file_names:
            with open(file, "r") as file:
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
            data = left[5:]
            file = right.strip()
            with open(file, "a") as file:
                file.write(data + "\n")
        elif ">" in command:
            left, right = command.split(">")
            data = left[5:].strip()
            filename = right.strip()
            with open(filename, "w") as file:
                file.write(data)
        else:
            data = command[5:]
            print(f"{data}")
    except FileExistsError:
        print("File Already exist.")


def move(command):
    try:
        part = command.split()
        destination = part[-1]
        if os.path.isdir(destination):
            files = part[1:-1]
            for source in files:
                new_destination = os.path.join(destination, os.path.basename(source))
                os.rename(source, new_destination)
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
        counter = len(part)
        files = part[1:-1]
        destination = part[-1]
        if os.path.isdir(destination):
            for source in files:
                dest_path = os.path.join(destination, os.path.basename(source))
                shutil.copy(source, dest_path)
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


def tree(path, prefix=""):
    data = os.listdir(path)
    for index, i in enumerate(data, start=0):
        full_path = os.path.join(path, i)
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
            tree(full_path, new_prefix)


def change_directory(command):
    try:
        if command == "~":
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
            for i in files:
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


def insensitive_grep(word, file_names):
    for file in file_names:
        with open(file, "r") as file:
            data = file.readlines()
        for line in data:
            if word.lower() in line.lower():
                print(line, end="")
        print("\n")


def count_grep(word, file_names):
    for file in file_names:
        count_num = 0
        with open(file, "r") as file:
            data = file.readlines()
        for line in data:
            show = line.count(word)
            count_num += show
        print(count_num)


def linenum_grep(word, file_names):
    found = False
    for file in file_names:
        with open(file, "r") as file:
            data = file.readlines()
        for index, line in enumerate(data, start=1):
            if word in line:
                found = True
                print(f"{index} . {line}", end="")
    print("\n")
    if not found:
        print("No line found contain this word.")


def grep(command):
    part = command.split()
    cmd = part[0]
    other = part[1:]
    try:
        found = False
        if other[0] in ["-c", "-n", "-i"]:
            new_part = other
            option_flag = new_part[0]
            word = new_part[1]
            file = new_part[2:]
            if option_flag == "-i":
                insensitive_grep(word, file)
            elif option_flag == "-c":
                count_grep(word, file)
            elif option_flag == "-n":
                linenum_grep(word, file)
        else:
            output = []
            new_part = other
            word = new_part[0]
            file_names = new_part[1:]
            for file in file_names:
                with open(file, "r") as f:
                    data = f.readlines()
                for line in data:
                    if word in line:
                        found = True
                        output.append(line)
                print("\n")
            if not found:
                print("No match file found.")
    except FileNotFoundError:
        print("File not found")
    return output


def head(command):
    try:
        part = command.split()
        file = part[1]
        with open(file, "r") as file:
            data = file.readlines()
            if len(data) > 10:
                for i in range(10):
                    print(data[i], end="")
            else:
                for line in data:
                    print(line, end="")
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
        with open(file, "r") as file:
            data = file.readlines()
        if len(data) > 10:
            reverse_data = data[-10:]
            for line in reverse_data:
                print(line, end="")
        else:
            for line in data:
                print(line, end="")
        print("\n")
    except FileNotFoundError:
        print("File doesn't Exist")
    except PermissionError:
        print("Access denied to this file.")
    except IsADirectoryError:
        print("It's a directory.")


def wc(command):
    part = command.split()
    cmd = part[0]
    file = part[1]
    try:
        with open(file, "r") as f:
            data = f.readlines()
        count_line = len(data)
        count_word = 0
        count_character = 0
        for line in data:
            words = line.split()
            count_word += len(words)
            for char in words:
                count_character += len(char)
        print(f"{count_line} {count_word} {count_character} {file}")
    except FileNotFoundError:
        print("File doesn't exist.")
    except IsADirectoryError:
        print("It's a directory.")
    except PermissionError:
        print("Access Denied to this file!")


def sorting(command):
    part = command.split()
    cmd = part[0]
    file_name = part[1]
    try:
        with open(file_name, "r") as file:
            data = file.readlines()
        sorted_data = sorted(data)
        for line in sorted_data:
            print(line, end="")
        print("\n")
    except FileNotFoundError:
        print("File doesn't exist.")
    except IsADirectoryError:
        print("It's a directory")
    except PermissionError:
        print("Access denied to this file!")
