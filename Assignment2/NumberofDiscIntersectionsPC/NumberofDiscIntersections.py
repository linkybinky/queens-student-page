#NumberofDiscIntersections
def solution(A):
    intersections = [] #Initialize intersection list
    for i in range(len(A)-1): #Loop through all but the last element
        for j in range(i+1,len(A)): #Loop through all elements after index i
            if i+A[i] >= j-A[j]: #If the upper limit (rightmost point in circle) of element i overlaps or is equal to the lower limit (leftmost point) in element j
                if {i,j} not in intersections: #Add the intersection if not already present already into intersections
                    intersections.append({i,j})
    return len(intersections) #Return the number of intersections



