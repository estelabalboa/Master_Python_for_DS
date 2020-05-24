#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Bunny:

    def __init__(self, n):
        self._n = n
    
    def __repr__(self):
        return f'The number of bunnies is {self._n} 🐰'

    def __str__(self):
        return f'The number of bunnies is {self._n}'

s = Bunny(47)
# print(repr(s))
# print(ascii(s)) # returns : The number of bunnies is 47 \U0001f430
print(repr(s)) # Returns the bunny emoji

print(ord('🐇'))

x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 10)
z = zip(x, y)

for a, b in z : print(f'{a} - {b}')

animals = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(animals): print(f'{i}: {v}')