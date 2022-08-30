#!/usr/bin/python3
def print_last_digit(number):

    last = 0
    if number > 0:
        last = number % 10
    elif number <= 0:
        last = (-1 * number) % 10
    elif number == 0:
        last = 0
    print("{}".format(last), end='')
    return(last)
