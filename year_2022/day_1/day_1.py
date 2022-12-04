import os


FILE_PATH = os.path.dirname(os.path.abspath(__file__))

def read_input(path) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()

def get_total_calories_per_elf(input: str) -> list[int]:

    elves = []
    # Read input
    _input = read_input(input)

    elf = []

    for line in _input:
        if not line.rstrip():
            elves.append(sum(elf))
            elf = []
            continue
        elf.append(int(line))

    return sorted(elves, reverse=True)

def results():
    file_path = os.path.join(FILE_PATH, "input.txt")

    elves = get_total_calories_per_elf(file_path)

    top_elf = elves[0]
    top_3_elves = sum(elves[:3])

    return top_elf, top_3_elves

