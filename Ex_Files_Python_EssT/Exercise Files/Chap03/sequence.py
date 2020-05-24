#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = ( 1, 2, 3, 4, 5 )
x = list(range(5))
x[2] = 24
for i in x:
    print('i is {}'.format(i))

# dictionary

x = {'one': 1, 'two': 2, 'three': 3}

for k, v in x.items():
    print('k: {}, v:{}'.format(k, v))