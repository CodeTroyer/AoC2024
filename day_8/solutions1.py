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


def is_valid_position(antenna, width, start, dx, dy):
    x = start[0]
    y = start[1]
    if 0 <= x - dx < width and 0 <= y - dy < width:
        coord = (x-dx, y-dy)
        if coord not in antenna:
            sub_antennas.add(coord)
    if 0 <= x + dx < width and 0 <= y + dy < width:
        coord = (x+dx, y+dy)
        if coord not in antenna:
            sub_antennas.add(coord)


def find_node(width, antenna):
    nr = len(antenna)
    for i in range(nr):
        for j in range(i+1, nr):
            first = antenna[i]
            second = antenna[j]
            dx = second[0] - first[0]
            dy = second[1] - first[1]
            is_valid_position(antenna, width, first, dx, dy)
            is_valid_position(antenna, width, second, dx, dy)

sub_antennas = set()

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    antennas = {}
    width = len(data)
    for r in range(len(data)):
        for c in range(len(data[r])):
            coord = (r,c)
            value = data[r][c]
            if value != ".":
                try:
                    antennas[value].append(coord)
                except KeyError:
                    antennas[value] = [coord]
    for antenna in antennas.values():
        find_node(width, antenna)
    print(len(sub_antennas))

if __name__ == "__main__":
    main()