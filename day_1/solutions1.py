
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

left = []
right = []


def main():
    total = 0
    data = file_utils.get_file_content(INPUT_FILE)
    for line in data:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        total += diff
    print(total)

if __name__ == "__main__":
    main()
