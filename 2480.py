n = int(input())
a = []
for i in range(n):
    a.append(input().split())
for j in range(n):
    for i in range(n-1, 0, -1):
        print(a[i][j], end = " ")
    print(a[i-1][j])