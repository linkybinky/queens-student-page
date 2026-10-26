def Solution(A):
    A.sort()
    count = 1
    #Iterate through a sorted list, returning 0 / False the moment the list stops being a permutated list
    for i in range(len(A)): 
        if A[i] == count:
            count +=1
        else:
            return 0
    return 1

A = [1,2,3,4,7,6]
print(Solution(A))