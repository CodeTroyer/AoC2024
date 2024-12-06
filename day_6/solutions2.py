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

def get_next_direction(direction):
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"

dir_dict = {
    "up": {"dx": 0, "dy": -1},
    "right": {"dx": 1, "dy": 0},
    "down": {"dx": 0, "dy": 1},
    "left": {"dx": -1, "dy": 0},
}

def check_loop(start, cells):
    direction = "up"
    running = True
    counter = 0
    while running:
        counter += 1
        if counter > 10000:
            return 1
        delta = dir_dict[direction]
        coord = start
        dx = delta["dx"]
        dy = delta["dy"]
        start = (coord[0] + dx, coord[1] + dy)
        try:
            val = cells[start]
            if val == "#":
                start = (coord[0], coord[1])
                direction = get_next_direction(direction)
            else:
                pass
        except KeyError:
            return 0


def main():
    data = file_utils.get_file_content(INPUT_FILE)
    cells = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            coord = (int(y), int(x))
            val = data[x][y]
            if val == "^":
                start = coord
                val = "X"
            cells[coord] = val
    loops = 0
    for cell in cells:
        val = cells[cell]
        if val == "#":
            pass
        elif val == "X":
            pass
        else:
            cells[cell] = "#"
            loops += check_loop(start, cells)
            cells[cell] = "."
    print(loops)

if __name__ == "__main__":
    main()
