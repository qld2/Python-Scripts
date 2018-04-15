def number = 1240;

import math

def is_prime(x) :
    for a in range(2, math.sqrt(x)) :
        if x%a == 0 :
            return 0
    return 1


for x in range(2, math.sqrt(number)) :
    if is_prime(x) == 1 :
        