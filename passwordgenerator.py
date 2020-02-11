#created by Joshua Evuetapha
'''
A program to generate strong password randomly
'''

import random

#length of the password 
LENGTH = 12

#list if characters used in generating the password
characters = ["0123456789", "!@#$%^&*", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"]

#empty password string
password = ""


for i in range(LENGTH):
     #choose a random index for the list
     index = random.randint(0, len(characters) - 1)
     #choose a random index for strings in the list
     index2 = random.randint(0, len(characters[index]) - 1)
     # concatenate the randomly generated character to the password string
     password += characters[index][index2]

#print the password 
print(password)
