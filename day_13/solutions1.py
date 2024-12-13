#!/usr/bin/env python3
import os
import sys
import re
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

def get_data():
    with open(INPUT_FILE, 'r') as file:
        return file.read()

def main():
    games = get_data().split("\n\n")
    game_dict = {}
    counter = 1
    total = 0
    for game in games:
        data = game.split("\n")
        for line in data:
            if "Button A" in line:
                ax = line.split("X+")[1].split(",")[0]
                ay = line.split("Y+")[-1]
            if "Button B" in line:
                bx = line.split("X+")[1].split(",")[0]
                by = line.split("Y+")[-1]
            if "Prize" in line:
                tx = line.split("X=")[1].split(",")[0]
                ty = line.split("Y=")[-1]
        game_dict[counter] = {"ax": int(ax), "ay": int(ay), "bx": int(bx), "by": int(by), "tx": int(tx), "ty": int(ty)}
        counter += 1
    for _, data in game_dict.items():
        tx = data['tx']
        ty = data['ty']
        ax = data['ax']
        ay = data['ay']
        bx = data['bx']
        by = data['by']
        x = (tx * by - ty *bx) / (ax * by - ay * bx)
        y = (tx - ax * x) / bx
        if x.is_integer() and y.is_integer():
            total += (x * 3 + y)
    print(int(total))

if __name__ == "__main__":
    main()
