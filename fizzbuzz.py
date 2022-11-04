#fizzbuzz program
for num in range(0,51):
    if num%3==0 and num%5==0:
        print('fizzbuzz')
    elif num%3==0:
        print('fizz')
    elif num%5==0:
        print('buzz')
    else:
        print(num)

# fibonacci sequence
def gen_fibon(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b,a+b

for num in gen_fibon(10):
    if num%2==0:
        print("This is part of a fibonacci sequence " + str(num))
    
#square generator
def gen_squares(n):
    for x in range(n):
        yield (x**2)

for num in gen_squares(10):
        print(num)


#random number generator
import random

def gen_random(low,high,n):
    for num in range(n):
        yield random.randint(low, high)

for i in gen_random(10, 200, 10):
    print("I am a randomly generated number " + str(i))                                                                                                                                       