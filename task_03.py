#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a loop"""

from decimal import Decimal


def lexicographics(to_analyze):
    """A function that returns a tuple for max, min and avg words.

    Args:
        to_analyze(mixed): number of words analyzed through diff functions.

    Returns:
        max (int): the maximum number of words per line.
        min (int): the minimum number of words per line.
        avg (decimal): the average number of words in dec.

    Examples:

        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling. ''')
        (5, 3, Decimal(4.0))
    """
    value = []
    lines = to_analyze.split("\n")

    for line in lines:
        calculate = line.split()
        value.append(len(calculate))

    minnum = min(value)
    maxnum = max(value)
    avgnum = Decimal(sum(value))/Decimal(len(value))
    return (minnum, maxnum, avgnum)
