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
        commands.cmd_list.append(command)
        with open(history_path, "a") as file:
            file.write(command + "\n")
        part = command.split()
        new_part = []
        for item in part:# wildcart
            if "*" in item or "?" in item or "[" in item:
                match = glob.glob(item)
                new_part.extend(match)
            else:
                new_part.append(item)
        part = new_part
        command = " ".join(part)
        command_pallete = {     #parser  content
            "exit":commands.exit,
            "cls" :commands.clear,
            "clear": commands.clear,
            "history":commands.history,
            "pwd":commands.pwd,
            "mkdir":commands.mkdir,
            "rmdir":commands.rmdir,
            "cd":commands.cd,
            "ls":commands.ls,
            "touch":commands.touch,
            "rm":commands.Remove,
            "cat":commands.cat,
            "echo":commands.echo,
            "mv":commands.move,
            "cp":commands.copy,
            "tree":commands.tree,
            "find":commands.find,
            "grep":commands.grep,
            "head":commands.head,
            "tail":commands.tail,
            "wc":commands.wc,
            "sort":commands.sorting
        }
        if "|" in command: #piped commands
            pipeline = command.split("|")
            pipe_commands  = {
                    "cat" : utils.cat_pipe,
                    "grep" : utils.grep_pipe,
                    "head" : utils.head_pipe,
                    "tail" : utils.tail_pipe,
                    "wc" : utils.wc_pipe,
                    "sort" : utils.sort_pipe,
                    "uniq" : utils.uniq_pipe,
                }
            returned_data = None
            for cmd_text in pipeline:
                part = cmd_text.split() 
                cmd = part[0].strip()
                args = part[1:]
                function = pipe_commands[cmd]
                returned_data = function(args, returned_data)
            commands.display_data(returned_data)
        elif ";" in command:
            command_lines = command.split(";")
            for cmd_text in command_lines:
                parts = cmd_text.split()
                cmd = parts[0].strip()
                function = command_pallete[cmd]
                data = function(cmd_text)
                if data is not None:
                    for line in data:
                        print(line)
                
        else:    #normal commad
            part = command.split()
            cmd = part[0]
            args = part[1:]
            if cmd in command_pallete:
                function = command_pallete[cmd]
                data = function(command)
                if data is not None:
                    for line in data:
                        print(line)
            else:
                print("Unknown command!")
    except Exception as e:
        print(e)
