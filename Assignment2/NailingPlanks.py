def solution(A,B,C):
    nailed = []
    for i in range(len(C)):
        for f in range(len(A)): 
            if C[i] >= A[f] and C[i] <= B[f]:
                if (f,A[f],B[f]) not in nailed:
                    nailed.append((f,A[f],B[f]))
                if len(nailed) == len(A):
                    return i+1
    return -1

A = [1, 4, 5, 8]
B = [4, 5, 9, 10]
C = [4, 6, 7, 10, 2]
print(solution(A, B, C))