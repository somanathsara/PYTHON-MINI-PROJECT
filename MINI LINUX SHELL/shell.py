import sys, os
import  shutil
import glob
import utils
import commands
SHELL_DIR = os.path.dirname(os.path.abspath(__file__))
history_path = os.path.join(SHELL_DIR, "history.txt")
help_path = os.path.join(SHELL_DIR, "help.txt")
print("MiniShell V1.O")
print("Type 'help' for commands: ")
cmdlist = []
while True:
    try:
        command = input(f"{os.getcwd()}\\MiniShell:>")
        cmdlist.append(command) # history
        with open(history_path, "a") as file:
            file.write(command + "\n")
        part = command.split()
        new_part = []
        for item in part:# wildcart
            if "*" in item or "?" in item or "[" in item:
                utils.expand_wildcards(command)
                match = glob.glob(item)
                new_part.extend(match)
            else:
                new_part.append(item)
        part = new_part
        command = " ".join(part)
        if "|" in command:#piped commands
            part = command.split("|")
            left = part[0].strip()
            right = part[1].strip()
            result = utils.cat_pipe(left)
            final_result = utils.grep_pipe(right[1],result)
            print(final_result)
        elif command == "exit":
            print("Exiting from Minishell.")
            sys.exit()
        elif command == "cls" or command == "clear":
            os.system("cls")
        elif command.lower() == "history":
            for i, cmd in enumerate(cmdlist, start=1):
                print(f"{i}.{cmd}")
        elif command == "pwd":
            print(os.getcwd())
        elif command == "ls":
            folders = os.listdir()
            for i in folders:
                print(i)
        elif command.startswith("cd"):
            part = command.split(maxsplit=1)
            if len(part) > 1:
                commands.change_directory(part[1])
            else:
                home = os.path.expanduser("~")
                os.chdir(home)
        elif command.startswith("mkdir"):
            if command == "mkdir":
                print("Missing folder operand!")
            else:
                folder = command[6:]
                if os.path.exists(folder):
                    print("Directory already exist. ")
                else:
                    os.mkdir(folder)
        elif command.startswith("rmdir"):
            if command == "rmdir":
                print("Missing folder operand")
            else:
                folder = command[6:]
                try:
                    os.rmdir(folder)
                    print("Directory removed Successfully.")
                except FileNotFoundError:
                    print("Directory doesn't exist")
                except OSError:
                    print("Directory is not empty. ")
        elif command.startswith("touch"):
            if command == "touch":
                print("Missing file operand!")
            else:
                commands.touch(command)
        elif command.startswith("rm"):
            if command == "rm":
                print("Missing file operand!")
            else:
                commands.Remove(command)
        elif command.startswith("cat"):
            if command == "cat":
                print("Missing file operand!")
            else:
                commands.cat(command)
        elif command.startswith("echo"):
            if command == "echo":
                print("Missing file operand!")
            else:
                commands.echo(command)
        elif command.startswith("mv"):
            if command == "mv":
                print("Missing file operand!")
            else:
                commands.move(command)
        elif command.startswith("cp"):
            if command == "cp":
                print("Missing file operand!")
            else:
                commands.copy(command)
        elif command.lower() == "help":
            with open(help_path, "r") as file:
                data = file.read()
            print(data)
        elif command == "tree":
            current_directory = os.getcwd()
            commands.tree(current_directory, "")
        elif command.startswith("find "):
            path = command[5:]
            commands.find(path)
        elif command.startswith("grep "):
            if ">" in command:
                utils.grep_redirection(command)
            datas = commands.grep(command)
            for data in datas:
                print(data)
        elif command.startswith("head"):
            if command == "head":
                print("Missing file oprand!")
            else:
                commands.head(command)
        elif command.startswith("tail"):
            if command == "tail":
                print("Missing file operand!")
            else:
                commands.tail(command)
        elif command.startswith("wc"):
            if command == "wc":
                print("Missing file opearand!")
            else:
                commands.wc(command)
        elif command.startswith("sort"):
            if command == "sort":
                print("Missing file operand!")
            else:
                commands.sorting(command)
        else:
            print("Unknown command! ")
    except Exception as e:
        print(e)
