#!/usr/bin/env python3
import os
import shutil

def generate_year_folder(year):
    if os.path.isdir(year):
        pass
    else:
        os.mkdir(year)


def generate_days(year):
    for day in range(1, 26):
        if len(str(day)) == 1:
            day = f"0{day}"
        folder = f"{year}/day_{day}"
        if not os.path.isdir(folder):
            os.mkdir(folder)
            generate_input_file(year, day)
            generate_solution_file(year, day)
        else:
            pass


def generate_input_file(year, day):
    file = f"{year}/day_{day}/input.txt"
    with open(file, "w") as f:
        pass


def generate_solution_file(year, day):
    destination = f"{os.path.dirname(__file__)}/{year}/day_{day}/"
    shutil.copy(f"{os.path.dirname(__file__)}/solutions.py", destination+"/solutions1.py")
    shutil.copy(f"{os.path.dirname(__file__)}/solutions.py", destination+"/solutions2.py")


def main():
    year = input("Provide year to generate: \n")
    generate_year_folder(year)
    generate_days(year)


if __name__ == "__main__":
    main()
