#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    x = [1, 2, 3, 4]
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'
    
    # funcions associated with a class are called methods, provides the interface to
    # the class and its objects
    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    
    # Changeing properties of the Class
    a0.sound('BARK')

    print(a0)
    print(a1)
    
    # Variable x is not encapsulated, exists in every instance of the class
    # underscore in a class is a convention to not touck this method
    print(a0.x)
    a0.x[0] = 'OTHER'
    print(a0.x)


if __name__ == '__main__': main()
