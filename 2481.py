n, m = map(int, input().split())
list = [list(map(int, input().split())) for i in range(n)]
c = []
for i in range(m):
    b = []
    for j in range(m - 1):
        for z in range(n - 1):
            b.append(list[j][i])
    c.append(b)
for i in c:
    k = -1
    for j in c:
        if i == j:
            k += 1
    if k > 0:
        print("YES")
        exit()
print("NO")