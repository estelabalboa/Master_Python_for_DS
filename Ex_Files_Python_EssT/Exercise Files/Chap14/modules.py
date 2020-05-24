#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    p = sys.platform
    print(f'System platform: {p}')

    o = os.name
    print(o)

    e = os.getenv('PATH')
    print(f'Environment: {e}')

    w = os.getcwd()
    print(f'Current working directory: {w}')

    x = list(range(25))
    print(x)
    import random
    random.shuffle(x)
    print(x)

if __name__ == '__main__': main()
