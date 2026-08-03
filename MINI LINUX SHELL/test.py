import os,commands
import glob,shutil
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
command = input("input:")
if ";" in command:
    command_lines = command.split(";")
    for cmd_text in command_lines:
        parts = cmd_text.split()
        cmd = parts[0].strip()
        function = command_pallete[cmd]
        data = function(cmd_text)
        if data is not None:
            for line in data:
                print(line)