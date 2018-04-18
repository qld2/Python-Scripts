#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0

#code
T = int(input())
    
def get_time(boards, partitions) :
    max = 0
    counter = 0
    i = 0
    j = 0
    
    while i < len(boards) :
        
        if i == partitions[j] :
            if counter > max :
                max = counter
            counter = 0
            j += 1
            
        counter += boards[i]
        i += 1
        
    return max
    
for t in range(0,T) :

    #inp = str(input()).split(' ')

    #k = int(inp[0])

    #n = int(inp[1])

    #boards = str(input()).split(' ')
    #boards = list(map(int, boards))
    
    #parts =  [[] * k]
    partitions = []
    times = []
    
    #print(boards)
    print(get_time([7, 9, 5, 5, 3], [1,2,4]))

    

