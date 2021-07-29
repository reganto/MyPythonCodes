#!/usr/bin/python
# -*- coding: utf-8

import glob

names = glob.glob("/home/reganto/*")

for obj in names:
    print(obj, end='\n')
