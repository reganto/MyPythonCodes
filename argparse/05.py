#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.prog = 'PROGRAM'
parser.description = 'This is a simple test for argparse module'

# parser.add_argument('--foo', type=int, choices=range(1, 4), required=True)
# parser.add_argument('bar', type=int, nargs='+')
parser.add_argument('--foo', nargs='?', dest='sample', metavar='YYY', help='foo for program')
#parser.add_argument('bar', nargs=2, metavar=('XXX', 'SSS'), help='bar fo %(prog)s')
group = parser.add_mutually_exclusive_group()
group.add_argument('-s', action='store_true')
group.add_argument('-d', action='store_true')
g = parser.add_argument_group('my group')
g.add_argument('--covar', action='store_const', const='0', default='1',
               dest='cov', metavar='covariance', help='covariance')
args = parser.parse_args()

print(args.sample)
print(args.s)
print(args.d)

