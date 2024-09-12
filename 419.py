def f(b):
    if b % 3 == 0:
        return b**2
    elif b % 3 == 1:
        return b
    else:
        return b // 3
n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += f(a[i])
print(sum