#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # def __init__(self, type, name, sound):
    #    self._type = type
    #    self._name = name
    #    self._sound = sound

    def __init__(self, **kwargs):
        # we can assign the default animal by the if condition
        self._type = kwargs['type'] if 'type' in kwargs else 'unicorn'
        self._name = kwargs['name'] if 'name' in kwargs else 'Elsa'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'riihn'


    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type='kitten', name='Fluffy', sound='rwar')
    a1 = Animal(type='duck', name='Donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    # print_animal(Animal('velociraptor', 'veronica', 'hello'))
    print_animal(Animal()) # taking default parameters

if __name__ == '__main__': main()
