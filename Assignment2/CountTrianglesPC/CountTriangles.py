def solution(A):
    A.sort() #Sort the array for easier processing
    count = 0 #Initialize count variable
    if len(A)<3: return 0 #Return invalid input
    for p in range(len(A)-2): #Iterate through the for each length in the triangle
        for q in range(p+1,len(A)-1):
            for r in range(q+1,len(A)):
                    if (A[p] + A[q]) > A[r] and (A[q] + A[r]) > A[p] and (A[r] + A[p]) > A[q]: #If all three elements are valid, add to count
                        count+=1
    return count
