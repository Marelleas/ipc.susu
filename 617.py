def NOD(A, B):
    if B == 0:
        return A
    else:
        return NOD(B, A % B)
A, B = map(int,input().split())
print(NOD(A, B))