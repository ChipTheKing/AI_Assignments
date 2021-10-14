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


if __name__ == '__main__':
    print(create_puzzle())
