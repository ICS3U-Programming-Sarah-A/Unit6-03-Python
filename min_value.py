#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 28th, 2022.
# This program generates a 10 random number between 0 and 100. It then uses a
# loop to display what position the random number is and then displays the
# lowest value.
import constants
import random


def find_min_value(some_array):
    min_value = 101
    min_value = some_array[0]

    # determines the min value
    for a_num in some_array:
        if a_num < min_value:
            min_value = a_num

    return min_value


def main():
    # initialize counter
    counter = 0

    # create an empty list
    num_random = []

    # displays & generates random numbers
    for counter in range(constants.MAX_SIZE):
        num_random.append(random.randint(constants.MIN_NUM, constants.MAX_NUM))

        print("{} is added to the list at position {}"
              .format(num_random[counter], counter))

    # call function & display the min value
    min_val = find_min_value(num_random)
    print("")
    print("The min value is: {}".format(min_val))


if __name__ == "__main__":
    main()
