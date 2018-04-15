#This is a coding project done from geeksforgeeks.org
#Specification can be found at:
#https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not/0

#code

T = int(input())

def equals(s1,s2) :
    if len(s1) != len(s2) :
        return 0;
    
    for i in range(0, len(s1)) :
        if s1[i] != s2[i] :
            return 0;
        
    return 1;

rotation = 0;
    
for i in range(0,T) :

    str1 = str(input())
    str2 = str(input())
    
    rotation = 0;
    
    for i in range(0, len(str1)) :
        str1 = str1[1:] + str1[0]
        
        if equals(str1, str2) == 1 :
            rotation = 1;
            
    print(rotation)
