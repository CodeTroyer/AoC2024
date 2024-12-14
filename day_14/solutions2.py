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


def reset_grid(rows, columns):
    for x in range(rows):
        for y in range(columns):
            grid[(x,y)] = 0


def print_grid(rows, columns):
    for x in range(rows):
        for y in range(columns):
            if grid[(x,y)] == 0:
                print(" ", end="")
            else:
                print(grid[(x,y)], end="")
        print("")


def has_horizontal_row(rows, columns):
    for row in range(rows):
        col_count = 0
        for column in range(columns):
            col_count += 1 if grid[(row, column)] != 0 else 0
            if col_count > 30:
                return True
    return False


def main():
    data = file_utils.get_file_content(INPUT_FILE)
    rows = 103
    columns = 101
    iterations = 10403
    trees = []
    for row in range(rows):
        for column in range(columns):
            grid[(row,column)] = 0

    print("Parsing all possible iterations...")
    for i in range(iterations):
        reset_grid(rows, columns)
        for line in data:
            sx, sy = map(int, line.split(" ")[0].split("=")[-1].split(","))
            vx, vy = map(int, line.split(" ")[-1].split("=")[-1].split(","))
            get_position(rows, columns, sx, sy, vx, vy, i)
        if has_horizontal_row(rows, columns):
            trees.append(i)

    print(trees)

    for tree in trees:
        print(f"Iteration {tree}")
        reset_grid(rows, columns)
        for line in data:
            sx, sy = map(int, line.split(" ")[0].split("=")[-1].split(","))
            vx, vy = map(int, line.split(" ")[-1].split("=")[-1].split(","))
            get_position(rows, columns, sx, sy, vx, vy, tree)
        print_grid(rows, columns)
        print(f"\nIteration: {tree}\n")
        wait = input()

if __name__ == "__main__":
    main()
