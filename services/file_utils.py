def get_file_content(file):
    with open(file) as f:
        return [line.strip('\n') for line in f.readlines()]


if __name__ == "__main__":
    print("Service module is not supposed to be called directly")
