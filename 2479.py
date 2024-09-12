n = int(input())
mat = []
ansmat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
    ansmat.append([0]*n)
for x in range(n):
    for y in range(n):
        ansmat[x][y] = mat[y][x]
for i in range(n):
    print(*ansmat[i])