#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys 

def main():
    print('Hello, World.')
    try:
        # x = int('foo')
        y = 5/0
    except ValueError: 
        print('I caight a value error')
    except:
        print(f'Unknown error: {sys.exc_info()[1]}')
    # except ZeroDivisionError:
    #    print('Don\'t divide by zero')

if __name__ == '__main__': main()
