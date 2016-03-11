#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a loop"""


def fibonacci(maxint):
    """A function returns a list of fibonacci sequence.

    Args:
        maxint (int): Upper bound of the loop. No default. Required.

    Returns:
        list: Sequence of numbers that is incremented to the next number.

    Examples:

        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

`       >>> fibonacci(22)
        [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """

    lastnum, curnum = 0, 1
    fibo_seq = [lastnum]
    while curnum < maxint:
        lastnum, curnum = curnum, lastnum + curnum
        fibo_seq.append(lastnum)
    return fibo_seq
