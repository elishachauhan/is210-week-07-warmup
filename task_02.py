#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a loop"""


def bool_to_str(bval):
    """A function that returns truthy or falsey values.

    Args:
        bval(bool): Uses True or False to return string values

    Returns:
        string: Results in Yes or No value

    Example:

        >>> bool_to_str(True)
        'Yes'

        >>> bool_to_str('')
        'No'
    """

    if bval:
        string = 'Yes'
    else:
        string = 'No'

    return string
