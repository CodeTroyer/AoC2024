#!/usr/bin/env python3
import os
import sys
import itertools
from itertools import product
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

def multiply(a, b):
    return a * b

def has_option(target, numbers):
    # print(target)
    operators = ["s", "m", "j"]
    options = [''.join(x) for x in product(operators, repeat=len(numbers)-1)]
    for option in options:
        total = 0
        counter = 0
        for operator in option:
            if counter == 0:
                if operator == "s":
                    total = numbers[counter] + numbers[counter + 1]
                elif operator == "m":
                    total = numbers[counter] * numbers[counter + 1]
                else:
                    concatenation = int(str(numbers[counter])+str(numbers[counter+1]))
                    total = concatenation
            else:
                if operator == "s":
                    total += numbers[counter + 1]
                elif operator == "m":
                    total *= numbers[counter + 1]
                else:
                    concatenation = int(str(total)+str(numbers[counter+1]))
                    total = concatenation
            counter += 1
        if total == target:
            return True
    return False

def is_valid(target, values):
    numbers = list(map(int,values.split(" ")))
    all_sum = sum(numbers)
    all_mul = 1
    for number in numbers:
        all_mul = multiply(all_mul, number)
    if all_sum == target:
        return target
    if all_mul == target:
        return target
    if has_option(int(target), numbers):
        return target
    return 0

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    total = 0
    for line in data:
        target, values = line.split(": ")
        total += is_valid(int(target), values)
    print(total)


if __name__ == "__main__":
    main()
