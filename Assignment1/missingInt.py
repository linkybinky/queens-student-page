def solution(A):
    #Sort the list so that the entire list can be parsed in order
    A.sort()
    missInt = 1
    #Parse through the list, discounting numbers smaller than 0
    for i in A: 
        if i > 0: 
            #If the number in the list is equal to MissInt, check if the next integer is missing
            if i == missInt:
                missInt+=1
            #If the number is not consecutive, it means that the missing Integer has been found, returning missInt
            if i > missInt:
                break
    return missInt

A = [1,3,6,4,1,2]
print(solution(A))
    

