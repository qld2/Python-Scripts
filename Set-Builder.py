#A method to iterate over all elements in the set:
#{(x_1, x_2, ... , x_n) in N^n : 
#            (n in N) and
#            (for all a in N between 1 and n - 1, x_a < x_(a + 1)) and
#            (n < k with k in N)}
#
# Intended to be used in the painters partition problem:

from sys import argv

numOfPainters = int(argv[1])
numOfBoards = int(argv[2])

def filler(arr, iterator, t, n, k) :
    
    if t == n + 3 :
        print(arr)
    else :
        for i in range(iterator + 1, k - n + t) :
            arr[t - 2] = i
            filler(arr , i, t + 1, n, k)
                
   
filler([0] * (numOfPainters - 1), -1, 2, numOfPainters - 2, numOfBoards - 1)
    
    