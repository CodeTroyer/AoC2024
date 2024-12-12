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
regions = []

def build_regions(point):
    region = [point]
    while len(current_list) > 0:
        point = current_list[0]
        x, y = point
        char = grid[point]
        up = grid.get((x-1, y), 0)
        down = grid.get((x+1, y), 0)
        left = grid.get((x, y-1), 0)
        right = grid.get((x, y+1), 0)
        already_checked.append(point)
        if up == char:
            if (x-1, y) not in already_checked:
                if (x-1, y) not in current_list:
                    current_list.append((x-1, y))
                    region.append((x-1, y))
        if down == char:
            if (x+1, y) not in already_checked:
                if (x+1, y) not in current_list:
                    current_list.append((x+1, y))
                    region.append((x+1, y))
        if left == char:
            if (x, y-1) not in already_checked:
                if (x, y-1) not in current_list:
                    current_list.append((x, y-1))
                    region.append((x, y-1))
        if right == char:
            if (x, y+1) not in already_checked:
                if (x, y+1) not in current_list:
                    current_list.append((x, y+1))
                    region.append((x, y+1))
        current_list.remove(point)
        points_to_check.remove(point)
    regions.append(region)

def calculate_cost(region, area):
    check_for_corner = set()
    for x, y in region:
        for nx, ny in [(x-0.5,y-0.5), (x+0.5,y-0.5), (x+0.5,y+0.5), (x-0.5,y+0.5)]:
            check_for_corner.add((nx,ny))
    sides = 0
    for nx, ny in check_for_corner:
        test = [(cx, cy) in region for cx, cy in [(nx-0.5,ny-0.5), (nx+0.5,ny-0.5), (nx+0.5,ny+0.5), (nx-0.5,ny+0.5)]]
        valid_tests = sum(test)
        if valid_tests == 1:
            sides += 1
        elif valid_tests == 2:
            if test == [True, False, True, False] or test == [False, True, False, True]:
                sides += 2
        elif valid_tests == 3:
            sides += 1
    return sides * area


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
        build_regions(current_list[0])

    for region in regions:
        total += calculate_cost(region, len(region))

    print(f"Total cost = {total}")

if __name__ == "__main__":
    main()
