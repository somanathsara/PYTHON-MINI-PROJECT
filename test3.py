# import glob
# files = glob.glob("*.txt")
# print(files)
import os
def move(command):
    
        part = command.split()
        destination = part[-1]
        if os.path.isdir(destination):
            files = part[1:-1]
            for source in files:
                new_destination = os.path.join(destination, os.path.basename(source))
            os.rename(source, new_destination)

    
move(input("Enter command here: "))