#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/container-with-most-water/0

T = int(input())
ans = []

for t in range(0,T) :
    n = int(input())
    
    numbers = []
    
    for i in range(0, n) :
        numbers.append(i + 1)

    counter = 1
    while len(numbers) > 1 :
        numbers.pop(counter)
        if counter + 1 < len(numbers) :
            counter += 1
        elif counter == len(numbers) :
            counter = 1
        else :
            counter = 0
    ans.append(numbers[0])
    
for t in range(0,T) :
    print(ans[t])
    