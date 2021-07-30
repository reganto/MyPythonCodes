#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

my_description = """
Convert torrent to direct link 
there are many example 
--> reganto [torrent file] 
--> reganto /tmp/sample.to
"""

parser = argparse.ArgumentParser(prog='Reganto', usage='%(prog)s [options]', description=my_description)
parser.add_argument('--foo', nargs='?', help='foo of the %(prog)s program')
parser.add_argument('bar', nargs='+', help='bar help')
parser.add_argument('apple', nargs='*', help='apple help for %(prog)s')
parser.print_help()

