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


def find_xmas(line):
    output = re.findall(r'XMAS', line)
    return len(output)

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    total = 0
    hor_lines = data
    r_hor_lines = [x[::-1] for x in data]
    ver_lines = []
    for i in range(len(data)):
        output = [x[i] for x in data]
        ver_lines.append("".join(output))
    r_ver_lines = [x[::-1] for x in ver_lines]

    max_col = len(data[0])
    max_row = len(data)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(data[y][x])
            rows[y].append(data[y][x])
            fdiag[x+y].append(data[y][x])
            bdiag[x-y-min_bdiag].append(data[y][x])
    f_diag = ["".join(x) for x in fdiag]
    r_f_diag = [x[::-1] for x in f_diag]
    b_diag = ["".join(x) for x in bdiag]
    r_b_diag = [x[::-1] for x in b_diag]
    for line in hor_lines:
        total += find_xmas(line)
    for line in r_hor_lines:
        total += find_xmas(line)
    for line in ver_lines:
        total += find_xmas(line)
    for line in r_ver_lines:
        total += find_xmas(line)
    for line in f_diag:
        total += find_xmas(line)
    for line in r_f_diag:
        total += find_xmas(line)
    for line in b_diag:
        total += find_xmas(line)
    for line in r_b_diag:
        total += find_xmas(line)
    print(total)


if __name__ == "__main__":
    main()
