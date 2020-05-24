#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5 

# while pw != secret:
#    count += 1 
#    if count > max_attempt: 
#        break
#    else :
#        pw = input(f"{count}: What's the secret word? ")
# else:
#    auth = True 

# print('Authorized' if auth else 'Calling the FBI..')

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog' : continue
    if pet == 'velociraptor' : break
    print(pet)
else:
    print('Taht is all of the animals')
