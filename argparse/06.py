#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


parser = argparse.ArgumentParser(prog='PROGRAM')
parser.add_argument('--foo', action='store_true', help='foo help')

subparsers = parser.add_subparsers(title='subcommands', description='This is a subcommands', help='sub-command help')
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

args = parser.parse_args()
print(vars(args))
