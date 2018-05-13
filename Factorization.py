from sys import argv
import math

number = int(argv[1])

def is_prime(x) :
    for a in range(2, int(math.sqrt(x)) + 1) :
        if x%a == 0 :
            return 0
    return 1

def factorize(x) :
    if is_prime(x) :
        return str(int(x)) + "."
    for i in range(2, int(math.sqrt(x)) + 1) :
        if is_prime(i) == 1 and x%i == 0 :
            return str(i) + ", " + factorize(x/i)
    return str()
    
print(factorize(number))