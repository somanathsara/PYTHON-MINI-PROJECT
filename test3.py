import os
import glob
new_part = []
command = input("input: ")
part = command.split()
wildcard = ['*', '?','[']
for item in part:
    if '*'in item :
                match = glob.glob(item)
                new_part.extend(match)
    else:
        new_part.append(item)
part = new_part
command = ""
for i in part:
    command.