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

left = []
right = []
left_dict = {}
right_dict = {}


def main():
    total = 0
    data = file_utils.get_file_content(INPUT_FILE)
    for line in data:
        l, r = line.split("   ")
        # if l in left_dict:
        #     left_dict[l] += 1
        # else:
        #     left_dict[l] = 1
        if r in right_dict:
            right_dict[r] += 1
        else:
            right_dict[r] = 1

    for line in data:
        l, r = line.split("   ")
        try:
            multi = right_dict[l]
        except KeyError:
            multi = 0
        score = int(l) * int(multi)
        total += score

    print(total)

if __name__ == "__main__":
    main()
