#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import math


parser = argparse.ArgumentParser()
parser.prog = 'PROGRAM'
parser.description = 'This is a simple test for argparse module'


def perfect_square(string):
    value = int(string)
    sqrt = math.sqrt(value)
    if sqrt != int(sqrt):
        msg = '{} is not a perfect square'.format(string)
        raise argparse.ArgumentTypeError(msg)
    return value


parser.add_argument('sqr', type=perfect_square)
parser.parse_args()

