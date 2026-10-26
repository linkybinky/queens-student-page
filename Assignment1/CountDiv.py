def solution(A, B, K):
    #initialize variables
    count = 0
    #Iterate through all numbers in between the two boundaries, counting each number that is divisble by K
    for i in range(A,B+1):
        if i % K  ==0:
            count+=1
    return count

print(solution(6,6,2))
