#CountDistinctSlices
def solution(M,A):
    slices = 0 #Initialize count variable
    tempslice = [] #Initialize temporary slice variable used to check validity
    for i in range(len(A)): #Iterate through all starting number
        tempslice.clear() #Clear validity checking slice each iteration
        for j in range(i,len(A)): #Iterate through possible end ranges
            if A[j] not in tempslice and A[j]<=M: #If valid, add to slice. If not, stop iterating for this start number
                tempslice.append(A[j])
                slices +=1
            else: break
    return slices

print(solution(6,[2,2,3,3]))

