#Passing Cars

def count_pairs(A):
    #initialize the number of 0's seen and the number of pairs
    seen0 = 0 
    pairs = 0
    #iterate through the array, adding the number the number of 0's seen to pairs per 1 seen
    for i in range(len(A)):
        if A[i] == 0:
            seen0 += 1
        else:
            pairs += seen0
    #check if the number of pairs exceeds 1,000,000,000 and return -1 if it does per assignment instructions
    if pairs > 1000000000:
        return -1
    else:
        return pairs
