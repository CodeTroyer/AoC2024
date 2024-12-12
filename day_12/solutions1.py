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

grid = {}
points_to_check = deque()
current_list = deque()
already_checked = deque()


def get_cost(point, fences, area):
    while len(current_list) > 0:
        point = current_list[0]
        x, y = point
        char = grid[point]
        up = grid.get((x-1, y), 0)
        down = grid.get((x+1, y), 0)
        left = grid.get((x, y-1), 0)
        right = grid.get((x, y+1), 0)
        fences += 4
        already_checked.append(point)
        if up == char:
            fences -= 1
            if (x-1, y) not in already_checked:
                if (x-1, y) not in current_list:
                    current_list.append((x-1, y))
                    area += 1
        if down == char:
            fences -= 1
            if (x+1, y) not in already_checked:
                if (x+1, y) not in current_list:
                    current_list.append((x+1, y))
                    area += 1
        if left == char:
            fences -= 1
            if (x, y-1) not in already_checked:
                if (x, y-1) not in current_list:
                    current_list.append((x, y-1))
                    area += 1
        if right == char:
            fences -= 1
            if (x, y+1) not in already_checked:
                if (x, y+1) not in current_list:
                    current_list.append((x, y+1))
                    area += 1
        current_list.remove(point)
        points_to_check.remove(point)
    return area * fences

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    total = 0
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            coord = (x,y)
            grid[coord] = char
            points_to_check.append(coord)
    while len(points_to_check) > 0:
        current_list.append(points_to_check[0])
        already_checked.append(points_to_check[0])
        total += get_cost(current_list[0], 0, 1)
    print(total)


if __name__ == "__main__":
    main()
