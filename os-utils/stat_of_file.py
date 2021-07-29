#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import stat	


def info(path):
    st = os.stat(path)
    print(st)

if __name__ == "__main__":
    info('/home/reganto')

