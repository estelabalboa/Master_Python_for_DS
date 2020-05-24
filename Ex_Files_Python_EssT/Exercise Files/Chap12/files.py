#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    import os 
    print(os.listdir())
    f = open('Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt', 'r')
    # for line in f:
    #    print(line.rstrip())
    print(f.readlines())
    
    f.close()

if __name__ == '__main__': main()
