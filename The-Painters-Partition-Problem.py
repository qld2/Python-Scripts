#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0

#code
from sys import argv

T = int(argv[1])
    
def get_time(boards, partitions) :
    max = 0
    sum = 0
    j = 0
    
    for i in range(0, len(boards)) :
        if i == partitions[j] :
            if sum > max :
                max = sum
            sum = 0
            
            if j < len(partitions)  - 1 :
                j += 1
        sum += boards[i]    
    return max
    
possiblePartitions = []    
    
def filler(arr, iterator, t, n, k) :
    
    if t == n + 3 :
        possiblePartitions.append(list(arr))
    else :
        for i in range(iterator + 1, k - n + t) :
            arr[t - 2] = i
            filler(arr , i, t + 1, n, k)
    
for t in range(0,T) :

    inp = str(argv[2]).split(' ')

    numOfPainters = int(inp[0])

    numOfBoards = int(inp[1])

    boards = str(argv[3]).split(' ')
    boards = list(map(int, boards))
    
    filler([0] * (numOfPainters - 1), -1, 2, numOfPainters - 2, numOfBoards - 2)
    
    min = 0
    
    print(get_time(boards, [1, 3]))
    
    for i in range(0, len(possiblePartitions)) :
        #time = get_time(boards, i)
        #if time < min :
        #    min = time
        print(possiblePartitions[i])
        print(get_time(boards, possiblePartitions[i]))    
    #print(min)

    

