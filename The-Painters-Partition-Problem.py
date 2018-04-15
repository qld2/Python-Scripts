#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/the-painters-partition-problem/0

#code
from sys import argv


T = argv[1]
inp = str(argv[2]).split(' ')

k = int(inp[0])

n = int(inp[1])

boards = str(argv[3]).split(' ')

boards = list(map(int, boards))

parts =  [[] * k]
partitions = []
times = []


def guess() : 
    total = 0
    for i in range(0, n) :
        total += boards[i]
    avg = total / k
	
    part = 0
    running_sum = 0
    for i in range(0, n) :
        if (running_sum < avg) & (part < k - 1) :
            parts[part].append(boards[i])
            running_sum += boards[i] 
        elif part == k - 1 :       
            parts[part].append(boards[i])
        else :
            parts.append([])
            partitions.append(i)
            part += 1
            parts[part].append(boards[i])
            running_sum = 0
    return parts

def calc_times() :
    for i in parts :
        sum = 0;
        for j in i :
            sum += j
        times.append(sum)


guess()
calc_times()

print(parts)
print(partitions)


           

    

