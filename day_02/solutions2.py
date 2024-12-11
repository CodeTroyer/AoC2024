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

def is_descending(lst):
    return all(int(lst[i]) >= int(lst[i+1]) for i in range(len(lst)-1))

def is_ascending(lst):
    return all(int(lst[i]) <= int(lst[i+1]) for i in range(len(lst)-1))

def get_increments(lst):
    return all(1 <= abs(int(lst[i]) - int(lst[i+1])) <= 3 for i in range(len(lst)-1))

def is_safe(numbers):
    down = is_descending(numbers)
    up = is_ascending(numbers)
    if down:
        if get_increments(numbers):
            return 1
    if up:
        if get_increments(numbers):
            return 1
    return 0

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    total = 0
    for line in data:
        numbers = line.split(" ")
        for i in range(len(numbers)):
            popped = numbers.pop(i)
            output = is_safe(numbers)
            if output:
                total += 1
                break
            else:
                numbers.insert(i, popped)
    print(total)


if __name__ == "__main__":
    main()
