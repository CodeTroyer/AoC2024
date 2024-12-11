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

def parse_number(inp):
    ret_list = []
    if inp == "0":
        ret_list.append("1")
        return ret_list
    if len(inp) % 2 == 0:
        left = inp[:len(inp) // 2]
        right = inp[len(inp) // 2:]
        ret_list.append(str(int(left)))
        ret_list.append(str(int(right)))
        return ret_list
    ret_list.append(str(int(inp)*2024))
    return ret_list

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    numbers = data[0].split(" ")
    old_list = numbers
    for blink in range(25):
        new_list = []
        for number in old_list:
            new_list.extend(parse_number(number))
        old_list = new_list
        print(f"Blink {blink+1}: {len(old_list)}")
    print(len(new_list))



if __name__ == "__main__":
    main()
