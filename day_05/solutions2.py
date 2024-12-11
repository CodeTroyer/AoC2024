#!/usr/bin/env python3
import os
import sys
import math
import functools
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

seen = {}

def correct_order(pages):
    for i in range(len(pages)):
            for j in range(i + 1, len(pages)):
                testing = (pages[i], pages[j])
                if testing in seen and seen[testing] == 1:
                     return False
    return True

def get_number(lst):
    length = len(lst)
    index = math.floor(length / 2)
    return lst[index]

def compare(x, y):
    return seen.get((x,y),0)

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    rules = []
    pages = []
    new_rule = True
    for line in data:
        if line == "":
            new_rule = False
        if new_rule:
            rules.append(line)
        else:
            pages.append(line)

    total = 0
    rule_list = []
    for line in rules:
        rule_list.append(list(map(int, line.split("|"))))

    for x, y in rule_list:
        seen[(x, y)] = -1
        seen[(y, x)] = 1

    for line in pages[1:]:
        page = list(map(int, line.split(",")))
        if not correct_order(page):
            page.sort(key=functools.cmp_to_key(compare))
            total += get_number(page)

    print(total)

if __name__ == "__main__":
    main()
