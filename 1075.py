m, n  = map(int, input().split())
a = list(range(n+1))
a[1] = 0
lst = []
i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
k = 0
for i in range(m, n+1):
    if i in lst:
        k += 1
print(k)