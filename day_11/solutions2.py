#!/usr/bin/env python3
import os
import sys
from functools import cache
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

@cache
def parse_number(number, blinks):
    if blinks == 0:
        return 1
    if number == 0:
        return parse_number(1, blinks-1)
    string = str(number)
    length = len(string)
    if length % 2 == 0:
        return parse_number(int(string[:length // 2]), blinks - 1) + parse_number(int(string[length // 2:]), blinks - 1)
    return parse_number(number * 2024, blinks - 1)

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    numbers = data[0].split(" ")
    print(sum(parse_number(int(number), 75) for number in numbers))


if __name__ == "__main__":
    main()
