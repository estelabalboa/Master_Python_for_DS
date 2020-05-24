#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n = 1):
    print(n)

function()

def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 5
if is_prime(n):
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')

def list_primes():
    for n in range(100):
        if is_prime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()