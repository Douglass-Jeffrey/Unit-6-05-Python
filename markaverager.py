#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Dec 2019
# This program calculates average of the marks with a passed list

import random


def average(marks):
    # This function calculates average of the marks with a passed list

    total = 0
    items = 0

    # process
    for number in marks:
        total = total + number
        items = items + 1

    # Calculates average
    average = total / items

    # output
    return round(average)


def main():
    # This takes the user's marks and passes them to average() in a list

    # This is a list to hold inputted marks
    marks = []
    final_average = 0
    mark = 0
    counter = 0

    # process
    try:
        while mark != -1:
            # input
            mark = int(input("Input " + "Mark " + str(counter + 1) + ": "))
            marks.append(mark)
            counter += 1

        marks.pop()

        final_average = average(marks)
        print("\nThe average of your " + str(counter - 1) + " marks is "
              + str(final_average) + "%")

    except Exception:
        print("Please input valid numbers")


if __name__ == "__main__":
    main()
