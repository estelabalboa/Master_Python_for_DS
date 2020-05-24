#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
f=1

def f1(f):
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

@f1 # decorator
def f3():
    print('this is f3')

# x = f1(f3)
# x()

# f3 = f1(f3)
# f3()

# using decorator to call it directly, wrapped 
f3()
