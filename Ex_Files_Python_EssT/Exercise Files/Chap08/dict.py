#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    
    easy_animals_dict = dict(kitten = 'meow',
                puppy = 'ruff!')

    animals = { 'kitten': 'meow',
                'puppy': 'ruff!', 
                'lion': 'grrr',
                'giraffe': 'I am a giraffe!', 
                'dragon': 'rawr' }

    print('found!' if 'lion2' in animals else 'NO!')
    print(animals.get('gozi'))
    print_dict(animals)
    print_dict(easy_animals_dict)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
