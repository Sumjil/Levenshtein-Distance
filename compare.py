A = input().lower()
B = input().lower()

    
    
def levenstain(A, B):
    F = []
    for i in range(len(B)+1):
        F.append([])
        for j in range(len(A)+1):
            if i==0 or j==0:
                F[i].append(i+j)
            else:
                F[i].append(0)
    
    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if A[j-1]==B[i-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1+min(F[i-1][j], F[i][j-1], F[i-1][j-1])
    return F[len(B)][len(A)]

print(levenstain(A,B)/(len(A)+len(B)))
    