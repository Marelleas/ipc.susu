n = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
for i in range(101):
    for j in range(n):
        if a[j] == i:
            b += 1
    if b > c:
        c = b
    b = 0
print(c)