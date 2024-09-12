n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
c = sum(a[0])
for i in range(n):
    sum = 0
    for j in range(n):
        sum += a[i][j]
    if sum != c:
        print("NO")
        exit()
for i in range(n):
    sum = 0
    for j in range(n):
        sum += a[j][i]
    if sum != c:
        print("NO")
        exit()
ac = 0
ab = 0
for i in range(n):
    ac += a[i][i]
    ab += a[n - i -1][n - 1 - i]
if ac == ab:
    print("YES")
else:
    print("NO")