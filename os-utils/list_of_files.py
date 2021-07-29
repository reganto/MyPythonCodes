#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Reganto
# Blog: reganto.net

import os

dirlist = os.listdir("/home/reganto/")
for item in dirlist:
    print(item, end='\n')

