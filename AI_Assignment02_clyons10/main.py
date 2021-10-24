# Christopher Lyons

# import statements initialization
import random


# function to create a random integer between 0 and 8
def random_integer():
    value = random.randint(0, 8)  # random integer function from the random class
    return value  # returns the random integer


# function to create a 3x3 list for the puzzle, numbers 0-8 will be randomized in their locations in the list
def create_puzzle():
    temp = []  # blank temporary list for number placement
    count = 0  # counting variable for the loop
    puzzle = []  # puzzle list variable initialization

    # loop to add numbers 0-8 into the temp list in random order without repeats
    while count < 9:  # loop runs until all 9 numbers are added into the list
        num = random_integer()  # function call to random_integer generates a new random number each loop iteration
        if num not in temp:  # control function that searches the temp list for the number to verify there is no repeats
            count += 1  # if the value of the random number isn't in the list count increases by 1
            temp.append(num)  # adds the number to the temp list

    # loop to take numbers from the temp list and store them in order into a 3x3 multi-dimensional list puzzle
    for x in range(3):  # loop runs 3 times to add values from temp into puzzle
        puzzle.append(temp[(x*3): ((x+1)*3)])  # each iteration, temp's values are added 3 at a time into puzzle
    return puzzle  # return completed 3x3 list


def move_up(puzzle, index_x, index_y):
    if index_x != 0:
        return puzzle_swap(puzzle, index_x, index_y, index_x + 1, index_y)
    else:
        return None


def move_down(puzzle, index_x, index_y):
    if index_x != 2:
        return puzzle_swap(puzzle, index_x, index_y, index_x - 1, index_y)
    else:
        return None


def move_left(puzzle, index_x, index_y):
    if index_y != 0:
        return puzzle_swap(puzzle, index_x, index_y, index_x, index_y - 1)
    else:
        return None


def move_right(puzzle, index_x, index_y):
    if index_y != 2:
        return puzzle_swap(puzzle, index_x, index_y, index_x, index_y + 1)
    else:
        return None


# function puzzle search looks through the multidimensional list for a given value
def puzzle_search(puzzle, value):
    x_index, y_index = 0, 0  # variable initialization
    # loop searches the list for the given value first by row and then by column
    for x in range(3):  # loop runs 3 times to look through each row in the list
        if value in puzzle[x]:  # if the given value is in the current row in the list then applies true
            x_index = x  # indexes the row value to x_index variable
            y_index = puzzle[x].index(value)  # indexes the column value using the list index into y_index variable
    return x_index, y_index  # return the two index values


# function for taking two locations in the puzzle and swapping their values
def puzzle_swap(puzzle, x1_index, y1_index, x2_index, y2_index):
    current_puzzle = puzzle  # initializes variable current_puzzle to the given list
    value1 = current_puzzle[x1_index][y1_index]  # stores the value at the location of the first index set to value1
    value2 = current_puzzle[x2_index][y2_index]  # stores the value at the location of the second index set to value2

    current_puzzle[x1_index][y1_index] = value2  # takes the first given index location and saves the second value there
    current_puzzle[x2_index][y2_index] = value1  # takes the second given index location and saves the first value there

    return current_puzzle  # returns the new puzzle list


# main function call
if __name__ == '__main__':
    # creates a 3x3 list with all of the values in the correct placement
    puzzle_goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    # function call to create_puzzle() to build a 3x3 list with the values in random locations
    initial_puzzle = create_puzzle()

    # print(puzzle_goal)  # print statement for the goal
    print(initial_puzzle)  # print statement for the randomized list
    print(puzzle_search(initial_puzzle, 0))  # prints the index values for the location of the value 0 in the list
    print(puzzle_swap(initial_puzzle, 0, 0, 2, 1))  # swaps the values at (0,0) and (2,1) and prints the result
