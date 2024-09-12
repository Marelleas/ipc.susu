def F(a):
    n = len(a)
    area = 0
    for i in range(n):
        x1, y1 = a[i]
        x2, y2 = a[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    area = abs(area) / 2.0
    return round(area, 1)


N = int(input())
a = []
for _ in range(N):
    x, y = map(int, input().split())
    a.append((x, y))
area = F(a)
print(area)