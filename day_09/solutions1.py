#!/usr/bin/env python3
import os
import sys
if os.path.isdir(f"/home/{os.getlogin()}"):
    UNIX = True
    sys.path.append(f"/home/{os.getlogin()}/Scripts/Advent of Code/services/")
else:
    UNIX = False
    sys.path.append("X:/Scripts/Advent of Code/services/")
import file_utils
import logic_utils

if UNIX:
    INPUT_FILE = "input.txt"
else:
    INPUT_FILE = f"{os.path.dirname(__file__)}/input.txt"


def main():
    data = file_utils.get_file_content(INPUT_FILE)
    file_id = 0
    diskspace = []
    for counter, value in enumerate(data[0]):
        val = int(value)
        if counter % 2 == 0:
            diskspace += [file_id for entry in range(val)]
            file_id += 1
        else:
            diskspace += ["." for entry in range(val)] # replace "empty" spaces with dots

    empty_index = [counter for counter, value in enumerate(diskspace) if value == "."]
    for index in empty_index:
        while diskspace[-1] == ".":
            diskspace.pop()
        move = diskspace.pop()
        try:
            diskspace[index] = move
        except IndexError:
            diskspace.append(move)

    print(sum(index * value for index, value in enumerate(diskspace)))


if __name__ == "__main__":
    main()
