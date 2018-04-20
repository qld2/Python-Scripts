#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/container-with-most-water/0

#code
T = int(input())
nL = []
L = []

def getArea(i1, i2) :
    return min(lines[i1],lines[i2]) * abs(i1 - i2)
        

for t in range(0, T) :
    nL.append(str(input()))

    lines = str(input())
    parsed = []
    
    #whitespace = false
    s = str()
    for i in lines :
        if i != ' ' :
            s += i
        else :
            parsed.append(s)
            s = str('')
        
    if s != '' :
        parsed.append(s)
    
    L.append(parsed)
    
    
for t in range(0,T) :
    numOfLines = int(nL[t])
    lines = []
    
    for i in L[t] :
        lines.append(int(i))
    
    max = 0;
    
    for i in range(0, numOfLines - 1) :
        if lines[i] != 0 & i < numOfLines :
            for j in range(i + 1, numOfLines) :
                area = getArea(i, j)
                if area > max :
                    max = area
    print(max)

