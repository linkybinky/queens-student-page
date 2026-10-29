def Solution(X, A):
    #Create dictionary with keys being locations and values noting if that location has leaves
    locations = {}
    for i in range(1,X+1):
        locations[i] = None
    #Iterate through A, noting down applicable locations and stopping the moment all locations have a leaf
    for i in range(0,len(A)):
        if A[i] in locations.keys():
            locations[A[i]] = i
            if None not in locations.values():
                #Returns the time (index +1) that all locations have leaves
                return i+1
    return -1

A = [1,3,1,4,2,3,5,4]
print(Solution(5,A))

