def maxsum(a, i1, j1, i2, j2):
    s = 0
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            s += a[i][j]
    return s

n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

x = a[0][0]
for i1 in range(n):
    for j1 in range(m):
        for i2 in range(i1, n):
            for j2 in range(j1, m):
                s = maxsum(a, i1, j1, i2, j2)
                if s > x:
                    x = s
print(x)