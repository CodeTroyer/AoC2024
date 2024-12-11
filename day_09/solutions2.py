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
    files = {}
    empty = []
    file_id = 0
    pos = 0

    for counter, value in enumerate(data[0]):
        val = int(value)
        if counter % 2 == 0:
            files[file_id] = (pos, val)
            file_id += 1
        else:
            if val != 0:
                empty.append((pos, val))
        pos += val

    while file_id > 0:
        file_id -= 1
        pos, size = files[file_id]
        for index, (start, length) in enumerate(empty):
            if start >= pos:
                empty = empty[:index]
                break
            if size <= length:
                files[file_id] = (start, size)
                if size == length:
                    empty.pop(index)
                else:
                    empty[index] = (start + size, length - size)
                break
    total = 0

    for file_id, (pos, size) in files.items():
        for entry in range(pos, pos + size):
            total += file_id * entry
    print(total)

if __name__ == "__main__":
    main()
