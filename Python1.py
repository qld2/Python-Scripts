import math

irrational = math.exp(1)
digits = 10;

factor = math.pow(10,digits - 1);

def is_prime(x) :
    for a in range(2, x-1) :
        if x%a == 0 :
            return 0
    return 1

irrational = irrational*factor

for x in range(1, 75) : 
    trun = math.floor(irrational) 
    if is_prime(trun) == 1 :
        print(trun)
    irrational = irrational/factor
    trun2 = math.floor(irrational)
    trun2 = trun2*factor
    irrational = irrational*factor
    irrational = irrational - trun2
    irrational = irrational*10