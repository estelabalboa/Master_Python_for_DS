#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt', 'rt')
    outfile = open('Ex_Files_Python_EssT/Exercise Files/Chap12/lines-copy-2.txt', 'wt')
    for line in infile:
        # print(line.rstrip(), file=outfile)
        outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
