
"""
Work on these problems with your group.
You will submit one solution for the entire group.

You should write the Python using only your group's knowledge and
the Python documentation (the "Docs" link on the CodeSkulptor page).

Full Names:
  Aravindakumar Sundaramraj
  Jeff Tang
  Kutub Gandhi
"""


#
# Predator-prey problem

# 1:
# Define the functions change_prey(birth, predation, prey, pred)
# and change_pred(growth, death, prey, pred), as described in the
# Lotka-Volterra Model video.
def change_prey(birth, predation, prey, pred):
    change_prey = (birth) * prey - predation * prey * pred
    return change_prey


def change_pred(growth, death, prey, pred):
    change_pred = (growth) * prey * pred - death * pred
    return change_pred


# 2:
# Define the function
# pred_prey(birth, predation, growth, death, prey, pred, num_timesteps)
# that computes the populations as described in the Lotka-Volterra
# Model video.  It returns a list of pairs of (prey, pred) populations.
#
# The input "num_timesteps" tells how many time periods that the simulation
# will run.  For example, each time step could be a year, and we could
# run the simulation for 20 years.  The various input rates are assumed
# to be rates per each time step.  The output list is of length
# "num_timesteps"+1 -- it has the populations at the beginning of the
# simulation, plus after each time step.

def pred_prey(birth, predation, growth, death, prey, pred, num_timesteps):
    preylist = [prey]
    predlist = [pred]
    store = [(prey, pred)]
    for i in range(num_timesteps):
        preylist.append(prey + change_prey(birth, predation, prey, pred))
        predlist.append(pred + change_pred(growth, death, prey, pred))
        prey = preylist[-1]
        pred = predlist[-1]
        store.append((prey, pred))
    return store


#
# Nested loops
# In the following, you'll want two loops, one nested inside the
# other.  Or, if you prefer, you can split it into two looping functions,
# with one calling the other repeatedly.


# 3:
# Define the function make_deck(cards, suits).  It takes a list of
# cards and a list of suits.  It returns a list of (card, suit) pairs.
# These pairs are ordered so that all the cards of one suit are
# together and that the pairs respect the ordering of the cards and suits.
#
# For example, make_deck([1, 2, 3], ["blue", "green"]) should return
# [(1, "blue"), (2, "blue"), (3, "blue"), (1, "green"), (2, "green"), (3, "green")].
#
# This notion of working with all possible pairs of elements is a common one.
def make_deck(cards, suits):
    store = []
    for i in suits:
        for j in cards:
            store.append((j, i))
    print store


# 4 (not tested by OwlTest):
# Define print_triangle(string) that takes a string and
# prints a triangle of prefixes, with letters separated by spaces.
#
# For example, print_triangle("hello") should print
#
# h
# h e
# h e l
# h e l l
# h e l l o
#
# Hint:  To print one thing and then later print another thing on the
# same line, use   "print something, "    -- Note the comma at the end.

def print_triangle(string):
    for i in range(len(string) + 1):
        print string[:i]
print_triangle('hello')

# 5:
# Define grade_all(solutions, answers).  "solutions" is a list of
# expected answers.  "answers" is a list of each student's list of
# answers, i.e., a list of lists of values.  You can assume that each
# student's list of answers is the same length as the list of solutions.
# You are to return a list of numbers, where each number is the
# number of correct answers for that corresponding student.
#
# For example, we can have three students and four problems:
# grade_all(['a', 'b', 'c', 'd'],
#           [['a', 'b', 'c', 'd'],
#            ['a', 'a', 'a', 'd'],
#            ['b', 'a', 'd', 'c']])
# should return [4, 2, 0].


def grade_all(solutions, answers):
    score = []
    for i in answers:
        for j in range(len(answers[i]) + 1):
            if answers[i][j] == solutions[j]:
                score.append(1)


#
# Removing selected elements from a list
#
# We often want to be able to remove selected elements from a list.
# For example, in a video game we might have a list of enemy ships, and
# we want to remove those that we've shot.
#
# The following examples illustrate some problems with removing
# elements and a simple way around such problems.


# 6 (not tested by OwlTest):
# Here are two attempts to remove elements.  Describe what each
# is doing and why it doesn't accomplish the intended task.
# Uncomment them to run them.
#
# Hint:  Try adding some print statements in the functions
# to see what is happening.

# def remove_elements1(input_list, elements_to_remove):
#    for idx in range(len(input_list)):
#        if input_list[idx] in elements_to_remove:
#            input_list.pop(idx)
#
# return input_list  # so that the function can be tested.
#
# numbers1 = range(10)
# numbers_to_remove1 = [3, 7, 2]
# remove_elements1(numbers1, numbers_to_remove1)
# print numbers1


# def remove_elements2(input_list, elements_to_remove):
#    for elt in input_list:
#        if elt in elements_to_remove:
#            input_list.remove(elt)
#
# return input_list  # so that the function can be tested.
#
# numbers2 = range(10)
# numbers_to_remove2 = [3, 7, 2]
# remove_elements2(numbers2, numbers_to_remove2)
# print numbers2


# 7:
# The easiest way around the problem is to completely avoid it.
# Rather than removing undesired elements, build a new list
# of the desired elements.
#
# A previous such example is filter_evens() from the previous
# class.  Go do that example if you haven't already.
#
# Define no_dups(a_list) that takes a list and returns a
# new list with the same elements in the same order, but
# without duplicates.  For example,
# no_dups([5, 8, 3, 5, 8, 2]) should return [5, 8, 3, 2].
def no_dups(a_list):
    pass
