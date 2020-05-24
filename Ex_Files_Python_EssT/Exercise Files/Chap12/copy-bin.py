#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('Ex_Files_Python_EssT/Exercise Files/Chap12/berlin.jpg', 'rb')
    outfile = open('Ex_Files_Python_EssT/Exercise Files/Chap12/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # to limit size
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
