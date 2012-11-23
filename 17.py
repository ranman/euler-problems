#!/usr/bin/env python

# How many letters would be needed to write all the numbers in words from 1 to 1000

# We use tuples because they're immutable and have less overhead than a list

# length of numbers 0-9
digits_len = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)
# length of teens 10-19
teens_len = (3, 6, 6, 8, 8, 7, 7, 9, 8, 8)
# length of prefix 0-90
tens_len = (0, 0, 6, 6, 5, 5, 5, 7, 6, 6)
and_len = 3
hundred_len = 7


def num_letters(num):
    total = 0



if __name__ == '__main__':
    print sum((num_letters(i) for i in xrange(1, 1000))) + 11
