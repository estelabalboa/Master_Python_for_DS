#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
x = 'seven'.upper()
print('x is {}'.format(x))
print(type(x))


y = 'seven "{1:<04}" "{0:>04}"'.format(8, 123)
print('y is {}'.format(y))
print(type(y))

# Integer and Floats
z = 7.0 // 3
print('z is {}'.format(z))
print(type(z))

m = .1 + .1 + .1 - .3
print('m is {}'.format(m))
print(type(m))

#Accuracy vs precision
from decimal import * 
a = Decimal('.10')
b = Decimal('.30')

m = a + a + a - b
print('m is {}'.format(m))
print(type(m))
print(id(m))

print('--------------------')

x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(id(x[2]))
print(id(y[2])) # different ids for tuple but same ids for equal elements

if x[1] is y[1]:
    print('yep')
else:
    print('noooo')

if isinstance(y, tuple):
    print(True)
elif isinstance(y, list):
    print(True, 'is a list')
else:
    print(False)

