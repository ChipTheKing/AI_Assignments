import random


def random_integer(high_value):
    value = random.randint(0, high_value)
    return value


def create_puzzle():
    temp = []
    count = 0
    puzzle = []

    while count < 9:
        num = random_integer(8)
        if num not in temp:
            count += 1
            temp.append(num)
    for x in range(3):
        puzzle.append(temp[(x*3): ((x+1)*3)])
    return puzzle


def puzzle_search(puzzle, value):
    x_index, y_index = 0, 0
    for x in range(3):
        if value in puzzle[x]:
            x_index = x
            y_index = puzzle[x].index(0)
    return x_index, y_index


def puzzle_swap(puzzle, x1_index, y1_index, x2_index, y2_index):
    current_puzzle = puzzle
    value1 = current_puzzle[x1_index][y1_index]
    value2 = current_puzzle[x2_index][y2_index]

    current_puzzle[x1_index][y1_index] = value2
    current_puzzle[x2_index][y2_index] = value1

    return current_puzzle


if __name__ == '__main__':
    puzzle_goal = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    initial_puzzle = create_puzzle()

    # print(puzzle_goal)
    print(initial_puzzle)
    print(puzzle_search(initial_puzzle, 0))
    print(puzzle_swap(initial_puzzle, 0, 0, 2, 1))
