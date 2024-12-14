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

grid = {}

def get_position(rows, columns, sx, sy, vx, vy, iterations):
    xmove = vx * iterations
    ymove = vy * iterations
    endx = (sx + xmove) % columns
    endy = (sy + ymove) % rows
    grid[(endy,endx)] += 1


def print_grid(rows, columns):
    for x in range(rows):
        for y in range(columns):
            print(grid[(x,y)], end="")
        print("")

def main():
    data = file_utils.get_file_content(INPUT_FILE)
    rows = 103
    columns = 101
    iterations = 100
    for row in range(rows):
        for column in range(columns):
            grid[(row,column)] = 0

    for line in data:
        sx, sy = map(int, line.split(" ")[0].split("=")[-1].split(","))
        vx, vy = map(int, line.split(" ")[-1].split("=")[-1].split(","))
        get_position(rows, columns, sx, sy, vx, vy, iterations)

    q1 = 0
    for x in range(rows // 2):
        for y in range(columns // 2):
            q1 += grid[(x,y)]
    q2 = 0
    for x in range(rows // 2 + 1, rows):
        for y in range(columns // 2):
            q2 += grid[(x,y)]
    q3 = 0
    for x in range(rows // 2):
        for y in range(columns // 2 + 1, columns):
            q3 += grid[(x,y)]
    q4 = 0
    for x in range(rows // 2 + 1, rows):
        for y in range(columns // 2 + 1, columns):
            q4 += grid[(x,y)]
    total = q1 * q2 * q3 * q4

    print(total)

if __name__ == "__main__":
    main()
