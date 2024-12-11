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


def find_xmas(letters, key):
    ndx = -1
    dx = 1
    ndy = -1
    dy = 1
    x, y = key
    try:
        a = letters[(x+dx,y+dy)]
        b = letters[(x+ndx, y+dy)]
        c = letters[(x+dx, y+ndy)]
        d = letters[(x+ndx, y+ndy)]
        if "X" in (a,b,c,d):
            return 0
        if a == "M" and b == "M" and c == "S" and d == "S":
            return 1
        if a == "M" and b == "S" and c == "M" and d == "S":
            return 1
        if a == "S" and b == "M" and c == "S" and d == "M":
            return 1
        if a == "S" and b == "S" and c == "M" and d == "M":
            return 1
        return 0
    except KeyError:
        return 0

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    total = 0
    letters = {}
    for i in enumerate(data):
        for j in enumerate(i[1]):
            letters[(i[0],j[0])] = j[1]
    for key, letter in letters.items():
        if letter == "A":
            total += find_xmas(letters, key)
    print(total)


if __name__ == "__main__":
    main()
