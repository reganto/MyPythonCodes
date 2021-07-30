#!/usr/bin.env python
# -*- coding: utf-8 -*-

import argparse
import sys


parser = argparse.ArgumentParser(
    prog='PROGRAM',
    description='sample description for program'
)

parser.add_argument('--infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('--outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('--num(s)', nargs='+')
parser.add_argument('--version', action='version', version='%(prog)s v2.0')
print(parser.parse_args('--num'.split()))

