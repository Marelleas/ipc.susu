p, q = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if abs(a[i]) % p == q:
        a[i] = 0
    print(a[i], end = " ")