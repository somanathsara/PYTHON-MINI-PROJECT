import os
import glob
import utils
command = input("input:")
if "|" in command:#piped commands
            part = command.split("|")
            left = part[0].strip()
            right = part[1].strip()
            result = utils.cat_pipe(left)
            final_result = utils.grep_pipe(right[1],result)
            print(final_result)