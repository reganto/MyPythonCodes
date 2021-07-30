#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def foo(args):
    print(args.x * args.y)


def bar(args):
    print('{}'.format(args.z))


parser = argparse.ArgumentParser()
parser.add_argument('--exit', action='store_true')
subparsers = parser.add_subparsers()

parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

args = parser.parse_args()
args.func(args)

if args.exit:
    parser.exit(0, 'exit program\n')

