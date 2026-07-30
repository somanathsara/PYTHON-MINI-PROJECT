# #grep command creation 'grep "word" filename'
# import os
# def grep(command):
#     part = command.split()
#     cmd = part[0]
#     other = part[1]
#     try:
#         found = False
#         if other.startswith("-"):
            
#         else:
#             new_part = other.split()
#             word =  new_part[0]
#             file = new_part[1]
#             with open(file, "r")as f:
#                 data = f.readlines()
#             for line in data:
#                 if word in line:
#                     found = True
#                     print(line,end ="")
#         if not found:
#             print("No match file found.")
#     except FileNotFoundError:
#         print("File not found")
#         # print(files)
# a = input("Enter command here: ")
# grep(a) 
a = "grep python file.txt"
part = a.split(maxsplit=1)
cmd = part[0]
other = part[1]
new_part = other.split()
# file = new_part[1]
# word = new_part[0]
# print(cmd, other, file, word)
# print(new_part)
print(cmd)
