#A method to iterate over all elements in the set:
#{(x_1, x_2, ... , x_n) in N^n : 
#            (n in N) and
#            (for all a in N between 1 and n - 1, x_a < x_(a + 1)) and
#            (n < k with k in N)}
#
# Intended to be used in the painters partition problem:

from sys import argv

k = int(argv[1])
n = int(argv[2])

end = []

for i in range(k - n + 1, k + 1) :
    end.append(i)

arr = [0] * n

for i in range(0, n) :
    arr[i] = i

    
#for i in range(0, k - n + 2) :
    
#    for j in range(i + 1, k - n + 3) :
        
#        for x in range(j + 1, k - n + 4) :
        
#            print([i,j,x])


#for i in range(0, k - n + 2) :
    
#    for j in range(i + 1, k - n + 3) :
        
#        for x in range(j + 1, k - n + 4) :
        
#            for y in range(x + 1, k - n + 5) :
            
#                print([i,j,x,y])


def filler(arr, iterator, t) :
    
    if t == n + 3 :
        print(arr)
    else :
        for i in range(iterator + 1, k - n + t) :
            arr[t - 2] = i
            filler(arr , i, t + 1)
                
   
filler([0,1,2,3], -1, 2)
   
#for t in range(2, 2 + n) :                
    
#    a = [] * n           
    
#    for i in range(t - 2, k - n + t) :
    
#        a.append(i)
        
#    print(a)
    
#while arr != end :
#    for i in range(0, n - 1) :
#    
#        if arr[i] < arr[i + 1] - 1 :
#            arr[i] += 1
#    if arr[n - 1] < k :
#        arr[n - 1] += 1
#        
#    print(arr)
    
    