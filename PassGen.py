

import random

print('Welcome to PassGen')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input('Enter amount of passwords to generate: '))

lenght = int(input('input lenght of passwords:'))

print('\nHere are your passwords...')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
    