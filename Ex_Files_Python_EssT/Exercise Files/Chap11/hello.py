#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7 * 1000 * 1000

print('The number is {:,}'.format(x).replace(',' , '.'))
print('The number is {:,.3f}'.format(x).replace(',' , '.'))