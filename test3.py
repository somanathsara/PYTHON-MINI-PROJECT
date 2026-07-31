import os
def wc(command):
    part = command.split()
    cmd = part[0]
    file = part[1]
    try:
        with open(file, "r")as f:
            data = f.readlines()
        count_line = len(data)
        count_word = 0
        count_character = 0
        for line in data:
            # print(line)
            words = line.split()
            count_word += len(words)
            for char in words:
                count_character += len(char)
        print(count_line, count_word, count_character, file)
    except Exception as e:
        print(e)
a = input("Enter command here: ")
wc(a)