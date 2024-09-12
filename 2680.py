def count(x, a):
    c = 0
    for i in range(len(a)):
        if a[i] == x:
            c += 1
    return c
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if not (count(a[i], a) > 2):
        b.append(a[i])
l = len(b)
print(l)
for i in range(l):
    print(b[i], end = " ")