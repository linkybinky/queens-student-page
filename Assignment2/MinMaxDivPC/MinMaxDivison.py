def solution(K,M,A):
    lower = max(A) #Initialize variables
    upper = sum(A)
    if K == 1: #Edge case of one box
        return upper
    if K >= len(A): #Edge case of equal or more boxes than elements in the array
        return lower
    while upper >= lower: #Binary search to find the lowest largest sum
        mid = (upper+lower)//2
        if isValid(A, mid,K):
            upper = mid-1
        else:
            lower = mid+1
    return lower

def isValid(A,maxBlockSize, maxBlockCount):
    blockSum = 0 #Initialize variables
    blockCount = 0
    for num in A: 
        if (blockSum + num) > maxBlockSize: #Iterate through numbers to create blocks that do not exceed proposed largest sum
            blockSum = num
            blockCount +=1
        else: 
            blockSum +=num
        if blockCount >= maxBlockCount: #If there are too many blocks created, then the proposed largest sum is too small
            return False
    return True #If there are enough blocks created, the proposed largest sum is too large

