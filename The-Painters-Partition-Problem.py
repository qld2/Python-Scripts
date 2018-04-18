#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0

#THIS IMPLEMENTATION OF A SOLUTION FAILS BECAUSE THE RECURSION TAKES FOREVER
#FOR LARGE TEST CASES AND THEREFORE FAILS THE AUTOGRADER. That being said i
#left this on here because filler is one of the coolest methods ive ever written.
#This still works for small test cases, like n < 9

#code
T = int(input())
nP = []
nB = []
B = []

for t in range(0, T) :
    inp = str(input()).split(' ')

    nP.append(int(inp[0]))

    nB.append(int(inp[1]))

    boards = str(input())
    parsed = []
    
    for i in boards :
        if (str(i) != '') & (i != ' ') :
            parsed.append(int(i))
    
    B.append(parsed)
    
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
        
    if sum > max :
        max = sum
        
    return max    
    
def filler(arr, iterator, t, n, k) :
    
    if t == n + 3 :
        possiblePartitions.append(list(arr))
    else :
        for i in range(iterator + 1, k - n + t) :
            arr[t - 2] = i
            filler(arr , i, t + 1, n, k)
    
for t in range(0,T) :
    numOfPainters = nP[t]
    numOfBoards = nB[t]
    boards = B[t]
    
    possiblePartitions = []
    filler([0] * (numOfPainters - 1), -1, 2, numOfPainters - 2, numOfBoards - 2)
    
    min = get_time(boards, possiblePartitions[0])
        
    for i in range(0, len(possiblePartitions)) :
        time = get_time(boards, possiblePartitions[i])
        if time < min :
            min = time
    print(min)

    

