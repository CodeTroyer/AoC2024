#!/usr/bin/env python3
import os
import sys
import re

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
    data = "".join(file_utils.get_file_content(INPUT_FILE))
    total = 0
    dos = data.split("do()")
    for entry in dos:
        parsing = entry.split("don't")[0]
        output = re.findall(r'mul\(\d{1,},\d{1,}\)', parsing)
        for entry in output:
            _, x = entry.split("(")
            y, _ = x.split(")")
            l, r = y.split(",")
            mul = int(l) * int(r)
            total += mul
    print(total)

if __name__ == "__main__":
    main()
