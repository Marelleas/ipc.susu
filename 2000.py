a, b = map(int, input().split())
k = 0
i = 1
while i <= 1000:
    c = i**3
    if (a <= c) and (c <= b):
        k += 1
    i += 1
print(k)