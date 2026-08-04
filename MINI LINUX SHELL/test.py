import os,commands
import glob,colorama,shutil
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
# command = input("input:")
# part = command.split("=")
# cmd = part[0].split()
# key = cmd[1]
# value = part[1]
# print(key)
# print(value)
# NAME= GUDU
# PROJECT= MINI LINUX SHELL
# HOME= G:/My drive/PYTHON SECURITY PROGRAMME
# PUSHED= Github
# name = ram
a = {"name":"arjun", "age":12}
a.pop("name")
print(a)
