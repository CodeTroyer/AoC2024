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
from collections import deque

if UNIX:
    INPUT_FILE = "input.txt"
else:
    INPUT_FILE = f"{os.path.dirname(__file__)}/input.txt"



def find_route(start, height):
    global total
    x, y = start
    height += 1
    points_to_check = deque([])
    dx = 1
    dy = 1
    px = int(grid.get((x+dx, y), -1))
    py = int(grid.get((x, y+dy), -1))
    nx = int(grid.get((x-dx, y), -1))
    ny = int(grid.get((x, y-dy), -1))
    if px == height:
        points_to_check.append((x+dx, y))
    if py == height:
        points_to_check.append((x, y+dy))
    if nx == height:
        points_to_check.append((x-dx, y))
    if ny == height:
        points_to_check.append((x, y-dy))
    if px == 9 and height == 9:
        total += 1
    if py == 9 and height == 9:
        total += 1
    if nx == 9 and height == 9:
        total += 1
    if ny == 9 and height == 9:
        total += 1
    while len(points_to_check) > 0:
        find_route(points_to_check[0], height)
        points_to_check.popleft()

global total
total = 0
grid = {}

def main():
    global total
    data = file_utils.get_file_content(INPUT_FILE)
    starting_points = []
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            coord = (i, j)
            if char == ".":
                char = -1
            grid[coord] = char
            if char == "0":
                starting_points.append(coord)
    for start in starting_points:
        find_route(start, 0)
    print(total)

if __name__ == "__main__":
    main()
