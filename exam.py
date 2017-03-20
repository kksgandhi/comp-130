import math
"""
Exam 1
"""

#
# GENERAL INSTRUCTIONS

# Text answers should be placed where indicated in this file in comments.

# Code style will be human-graded.  This includes good variable names and
# not having over-complicated code.  This also includes having appropriate
# docstrings for any functions that you add.  Additional comments are only
# needed as necessary to explain your code.

# Unless otherwise specified, do not mutate the input.
# This is not typically checked by the given tests, but points will be
# deducted if you mutate the input.

# Tests are provided in this code file.  We have not set up OwlTest
# for this exam.  Do not change any of the test code.


#
# Test support code
# DO NOT EDIT.
#
HIDE_ERRORS = False     # False = Errors reported normally.  True = Errors simply fail tests.
points_earned = 0
points_possible = 0


def test(points, test_name, fn, args, expected):
    """Test function, print results, and keep track of points."""
    global points_earned
    global points_possible

    # Test function
    fail = False
    if HIDE_ERRORS:
        # If error occurs, just fail test, and continue.
        try:
            result = fn(*args)
        except:
            fail = True
            result = "ERROR"
    else:
        # If error occurs, let it be reported normally for debugging.
        result = fn(*args)
    if not fail:
        if ((isinstance(expected, float) and round(result, 6) != round(expected, 6)) or
                (not isinstance(expected, float) and result != expected)):
            fail = True

    # Print results, and keep track of points
    points_possible += points
    if fail:
        print - \
            points, "Failed", test_name, "Expected:", expected, "Result:", result
    else:
        print "Passed", test_name
        points_earned += points


#
# Part 1
#
# We have a pet snail named Slimy that we have trained to follow
# some simple directions.  You'll write a program that simulates
# the results of Slimy's behavior as he wanders around his
# play area.
#
# We'll model his play area as a rectangular grid, represented
# in Python as a list of lists of characters (i.e., length one
# strings).  Those strings represent what is one the ground
# at each location in the grid.  A space character (' ')
# represents an empty spot in the grid.
#
# Note that you are not allowed to use CodeSkulptor's numeric
# module for representing the grid.
#


#
# Problem 1
# 15 points total
#    14 points correctness -- 4 points empty grid, 10 points non-empty grid
#     1 point  style
#
# We want a way to display the simulation results.
# For simplicity, we'll just print some results in
# CodeSkulptor's output pane.  However, we need a
# function to put the grid into a nicely printable form.
#
# Complete the following function, as described by its
# documentation string.

def format_grid(grid):
    """
    Returns a string representation of the entire grid.
    All of the characters in a row are concatenated,
    along with a row-ending newline.
    All of the rows are concatenated.
    """
    return_string = ""
    for row in grid:
        for element in row:
            return_string += element
        return_string += "\n"
    return return_string


#
# DO NOT EDIT THIS TESTING CODE.
# test(#points, description, function, list of arguments, expected output)
test(2, "No rows or cols",
     format_grid,
     [[]],
     "")
test(2, "No cols",
     format_grid,
     [[[],
      [],
      []]],
     "\n\n\n")
test(3, "3-by-1",
     format_grid,
     [[['a'],
      ['b'],
      ['c']]],
     "a\nb\nc\n")
test(3, "1-by-3",
     format_grid,
     [[['a', 'b', 'c']]],
     "abc\n")
test(4, "4-by-2",
     format_grid,
     [[['z', 'a'],
       ['z', 'b'],
       ['z', 'c'],
       ['z', 'd']]],
     "za\nzb\nzc\nzd\n")


#
# Problem 2
# 15 points total
#    14 points correctness -- 4 points base case, 5 points rectangular case, 5 points other case
#     1 point style
#
# Complete the following function, as described by its
# documentation string.

def is_rectangular_grid(grid):
    """
    Returns whether the given grid (list of lists) is
    rectangular, i.e., whether every row is of the same
    length.

    A grid with no rows is considered rectangular.

    Assumes that the grid is a list of lists.
    """
    if(len(grid) == 0):
        return True
    init_grid_len = len(grid[0])
    for row in grid:
        if(init_grid_len != len(row)):
            return False
    return True

#
# DO NOT EDIT THIS TESTING CODE.
# test(#points, description, function, list of arguments, expected output)
test(2, "no rows or cols",
     is_rectangular_grid,
     [[]],
     True)
test(2, "no cols",
     is_rectangular_grid,
     [[[],
      [],
      [],
      []]],
     True)
test(1.5, "3-by-1",
     is_rectangular_grid,
     [[['a'],
      ['b'],
      ['c']]],
     True)
test(1.5, "1-by-3",
     is_rectangular_grid, [[['a', 'b', 'c']]],
     True)
test(2, "4-by-2",
     is_rectangular_grid,
     [[['y', 'z'],
      ['y', 'b'],
      ['y', 's'],
      ['y', 'n']]],
     True)
test(2.5, "one longer",
     is_rectangular_grid,
     [[['a'],
      ['b', 'z'],
      ['c']]],
     False)
test(2.5, "one shorter",
     is_rectangular_grid,
     [[['y', 'z'],
      ['a', 'b'],
      ['r', 's'],
      ['m']]],
     False)


#
# Problem 3
# 27 points total
#    20 points correctness
#     5 points recipe
#     2 points style
#
# Simulates one type of instruction that Slimy
# understands.
#     Goes n locations forwards.  If he
#     bumps into the boundary of his play area, he just
#     stays in place.
#
# When Slimy moves, he leaves slime on the ground.
# That is represented in the grid by the string '#'.
# Slimy's current location is represented by the
# string 'S'.
#
# We keep track of Slimy's position as a pair of
# row and column numbers.
#
# We keep track of Slimy's direction as a number.
# We choose 0=up/north, 1=right/east, 2=down/south,
# 3=left/west.


# Write your recipe here in comments:
"""
I am too lazy to write a bunch of if statements about how the directions map to variable addition,
So I will write a dictionary that maps each direction to a +/- value (look at the code I write, it makes sense
in my head but I am having trouble explaining it in the recipe). Thanks
Example: 0 will map to -1 in the up/down direction because a 0 means you should move upward, aka -1
I will enumerate a number of times as given in the inputs.
I will keep track of slimy's position using the position input
Each loop, I will put slime at slimy's position
I will then increase or decrease the position list using my previously made mapping dictionaries
I will use min and max to ensure that slimy does not escape his cage
if slimy is outside of his cage, his position will be forced back into the cage by min and max
I might write a function for that.
After all the slime laying and position moving is done, I will put an S at slimy's
final position to indicate that
I will then return the final position
"""


def slimy_stay(num, min_val, max_val):
    """
    Returns num, bounded by min and max val
    """
    return max(min_val, min(num, max_val))


def simulate_slimy_go(grid, n, position, direction):
    """
    Mutates grid as Slimy moves forward n locations,
    starting at the current position and in the given
    direction.
    Returns the new position.

    Assumes grid is rectangular grid represented by
    a list of lists of single characters.
    Assumes starting position is in grid and has an 'S'.
    """
    up_down_dict = {0: -1, 1: 0, 2: 1, 3: 0}
    left_right_dict = {0: 0, 1: 1, 2: 0, 3: -1}
    position_list = list(position)
    for _enumerate in range(n):
        grid[position_list[0]][position_list[1]] = '#'
        position_list[0] += up_down_dict[direction]
        position_list[0] = slimy_stay(position_list[0], 0, len(grid) - 1)
        position_list[1] += left_right_dict[direction]
        position_list[1] = slimy_stay(position_list[1], 0, len(grid[0]) - 1)
    grid[position_list[0]][position_list[1]] = 'S'
    return (position_list[0], position_list[1])


#
# DO NOT EDIT THIS TESTING CODE.
# test(#points, description, function, list of arguments, expected output)
SAMPLE_4BY5_GRID = [[' ', ' ', ' ', ' ', ' '],
                    [' ', 'S', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ']]
SAMPLE_4BY5_POSN = (1, 1)
test(1, "north 0",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 0, SAMPLE_4BY5_POSN, 0],
     SAMPLE_4BY5_POSN)
test(2, "north into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 2, SAMPLE_4BY5_POSN, 0],
     (0, 1))
test(2, "north not into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 1, SAMPLE_4BY5_POSN, 0],
     (0, 1))
test(1, "east 0",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 0, SAMPLE_4BY5_POSN, 1],
     SAMPLE_4BY5_POSN)
test(2, "east into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 5, SAMPLE_4BY5_POSN, 1],
     (1, 4))
test(2, "east not into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 2, SAMPLE_4BY5_POSN, 1],
     (1, 3))
test(1, "south 0",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 0, SAMPLE_4BY5_POSN, 2],
     SAMPLE_4BY5_POSN)
test(2, "south into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 4, SAMPLE_4BY5_POSN, 2],
     (3, 1))
test(2, "south not into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 1, SAMPLE_4BY5_POSN, 2],
     (2, 1))
test(1, "west 0",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 0, SAMPLE_4BY5_POSN, 3],
     SAMPLE_4BY5_POSN)
test(2, "west into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 3, SAMPLE_4BY5_POSN, 3],
     (1, 0))
test(2, "west not into wall",
     simulate_slimy_go,
     [SAMPLE_4BY5_GRID, 1, SAMPLE_4BY5_POSN, 3],
     (1, 0))


#
# Problem 4
# 5 points total
#    3 points correctness
#    2 points style
#
# Simulates one type of instruction that Slimy
# understands.
#     Turn right n times without changing
#     location.  Each turn is 90 degrees, so that Slimy
#     only faces east, south, west, or north.
#
# Hint:  Observe how turning right changes the direction.

def simulate_slimy_turn(n, direction):
    """
    Returns the new direction of Slimy after turning
    right n times.
    """
    return (direction + n) % 4
    pass


#
# DO NOT EDIT THIS TESTING CODE.
# test(#points, description, function, list of arguments, expected output)
test(0.5, "no turn from east",
     simulate_slimy_turn,
     [0, 1], 1)
test(0.5, "no turn from west",
     simulate_slimy_turn,
     [0, 3], 3)
test(1, "two turns from south",
     simulate_slimy_turn,
     [2, 3], 1)
test(1, "seven turns from north",
     simulate_slimy_turn,
     [7, 0], 3)


#
# Problem 5
# 15 points total
#    14 points correctness
#     1 point  style
#
# Slimy is a very smart snail.  He can count,
# and he can understand two kinds of instructions.
# Each instruction is a tuple:
# ('go', n) -- Goes n locations forwards.  If he
#     bumps into the boundary of his play area, he just
#     stays in place.
# ('turn', n) -- Turn right n times without changing
#     location.  Each turn is 90 degrees, so that Slimy
#     only faces east, south, west, or north.
# Slimy ignores any other instruction.
# Slimy takes a list of instructions.
#
# We keep track of Slimy's position as a pair of
# row and column numbers.
#
# We keep track of Slimy's direction as a number.
# We choose 0=up/north, 1=right/east, 2=down/south,
# 3=left/west.

def simulate_slimy(grid, instructions):
    """
    Simulates the behavior of Slimy the pet snail.
    Slimy starts with the given grid.
    Slimy starts at row 0, column 0, facing right/east.
    Slimy obeys the given list of instructions.
    The simulation mutates the grid as Slimy moves, and
    returns the resulting grid.

    If the given grid does not have a row 0, column 0,
    or if the given grid is not rectangular,
    then the simulation stops and returns None.

    Assumes that the grid is a list of lists,
    that instructions is a list of pairs, and that
    each instruction has a non-negative integer.
    """
    if(len(grid) == 0 or len(grid[0]) == 0):
        return
    if not is_rectangular_grid(grid):
        return
    position = [0, 0]
    direction = 1
    for instruction in instructions:
        if(instruction[0] == 'go'):
            position = list(
                simulate_slimy_go(grid,
                                  instruction[1],
                                  (position[0],
                                   position[1]),
                                  direction))
        elif(instruction[0] == 'turn'):
            direction = simulate_slimy_turn(instruction[1], direction)
    return grid


#
# DO NOT EDIT THIS TESTING CODE.
# test(#points, description, function, list of arguments, expected output)
test(1, "no rows or cols",
     simulate_slimy,
     [[], []],
     None)
test(1, "no cols",
     simulate_slimy,
     [[[],
       [],
       []],
      []],
     None)
test(1, "not rectangular",
     simulate_slimy,
     [[['a', 'b'],
       ['c', 'd', 'e'],
       ['f', 'g']],
      []],
     None)
test(1, "no instructions",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']], []],
     [['S', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ']])
test(1, "go not into wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('go', 2), ('go', 1)]],
     [['#', '#', '#', 'S', ' '],
      [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']])
test(1, "go into wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('go', 16)]],
     [['#', '#', '#', '#', 'S'],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ']])
test(2, "turn",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('turn', 16)]],
     [['S', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ']])
test(2, "go and turn not into wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('turn', 5), ('go', 2), ('turn', 3), ('go', 3), ('turn', 1), ('go', 1),
       ('turn', 2), ('go', 2)]],
     [['#', ' ', ' ', ' ', ' '],
      ['#', ' ', ' ', 'S', ' '],
      ['#', '#', '#', '#', ' '],
      [' ', ' ', ' ', '#', ' ']])
test(1, "go and turn into N wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('go', 2), ('turn', 3), ('go', 1)]],
     [['#', '#', 'S', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ']])
test(1, "go and turn into E wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('go', 2), ('turn', 1), ('go', 1), ('turn', 3), ('go', 6)]],
     [['#', '#', '#', ' ', ' '],
      [' ', ' ', '#', '#', 'S'],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ']])
test(1, "go and turn into W wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('go', 2), ('turn', 2), ('go', 5)]],
     [['S', '#', '#', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ']])
test(1, "go and turn into S wall",
     simulate_slimy,
     [[['S', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ', ' ']],
      [('go', 2), ('turn', 1), ('go', 15)]],
     [['#', '#', '#', ' ', ' '],
      [' ', ' ', '#', ' ', ' '],
      [' ', ' ', '#', ' ', ' '],
      [' ', ' ', 'S', ' ', ' ']])


#
# Part 2
#
# Dr. Freud has given a psychological survey to a bunch
# of students.  Since he's most interested in various
# abnormal behaviors, he wants to find out which surveys
# have atypical scores.  Following the ideas of a bell
# curve, typical scores are those that are near the mean,
# while atypical scores are those that are far from the
# mean.  As is common, "near" and "far" are thought of
# in terms of how the distance relates to the standard
# deviation of the scores.
#
# As a reminder, the standard deviation of a population
# is the square root of the variance.
#

#
# Provided code -- As seen in Assignment 3 Statistics
# DO NOT EDIT.
#

def arithmetic_mean(num_list):
    """
    Returns the arithmetic mean of the numbers in the list.
    Returns None if the list is empty.
    """

    if num_list:
        return float(sum(num_list)) / len(num_list)
    else:
        return None


def square_differences(num_list, value):
    """
    Returns a new list where each element is the square of the
    difference between a list element and the given value.
    """

    sqdiffs = []
    for num in num_list:
        sqdiffs.append((num - value) ** 2)
    return sqdiffs


def pop_variance(num_list):
    """
    Returns the population variance of the numbers in the list.
    Returns None if the list is empty.
    """

    if num_list:
        return arithmetic_mean(square_differences(num_list, arithmetic_mean(num_list)))
    else:
        return None


#
# Problem 6
# 15 points total
#    14 points correctness
#     1 point  style
#
# Complete the following function, as described by its
# documentation string.
def atypical_scores(scores, n):
    """
    Given a dictionary mapping people's names to scores,
    returns a dictionary of those people and scores that
    are more than n standard deviations away from the mean.

    If there are no scores, then returns the empty list,
    since none are atypical.
    """
    if(len(scores) == 0):
        return {}
    return_dict = {}
    scores_list = []
    for key in scores:
        scores_list.append(scores[key])
    variance = pop_variance(scores_list)
    mean = arithmetic_mean(scores_list)
    std = math.sqrt(variance)
    for person in scores:
        if(math.fabs(scores[person] - mean) > std * n):
            return_dict[person] = scores[person]
    return return_dict


#
# DO NOT EDIT THIS TESTING CODE.
# test(#points, description, function, list of arguments, expected output)
SAMPLE_SCORES = {'John': 50, 'Mary': 70, 'Sue': 80, 'Scott': 75, 'Joe': 30,
                 'Bill': 100, 'Bob': 82, 'Anna': 86, 'Lori': 74}

test(2, "no data",
     atypical_scores,
     [{}, 3],
     {})
test(4, "0 stddev",
     atypical_scores,
     [SAMPLE_SCORES, 0],
     SAMPLE_SCORES)
test(4, "1 stddev",
     atypical_scores,
     [SAMPLE_SCORES, 1],
     {'Joe': 30, 'John': 50, 'Bill': 100})
test(4, "2 stddev",
     atypical_scores,
     [SAMPLE_SCORES, 2],
     {'Joe': 30})


#
# Part 3
#
# Short-answer problem
# Provide your answer in comments.
#

#
# Problem 7
# (8 points)
#
# Explain what the point of writing a "recipe" is
# and why you should write it before writing code.
"""
code is difficult, I know because I have been writing code for the last few hours
Most of the time, code involves a series of interconnecting steps that you can't just keep straight in your head
In addition, code can (and should) be broken down into smaller chunks that are completed individually.
Recipes serve to break code down into smaller chunks, and also to keep them straight in your head
Each sentence in a recipe should be a few lines of code, a simple task that can't really be broken down further
It should be a plain English algorithm for completing your task, if it was given to a human instead of a computer
When you are ready to turn your recipe into code, go through each sentence in your recipe
and implement it in your language of choice.
Just go line by line down your recipe and it should be easy to make it into code

Recipes also help to make you see the big picture
Writing a recipe is a good way to find flaws in your overall algorithm.
"""

print "\n\nTentative correctness score (may be modified by grader):"
print points_earned, "of", points_possible


print "\nGrading not automated:"
print "Short answer: (13 points total)"
print "   5 points: simulate_slimy_go recipe"
print "   8 points: recipe explanation"
print "Style:        ( 8 points total)"
print "   1 point : format_grid"
print "   1 point : is_rectangular_grid"
print "   2 points: simulate_slimy_go"
print "   2 points: simulate_slimy_turn"
print "   1 point : simulate_slimy"
print "   1 point : atypical_scores"
