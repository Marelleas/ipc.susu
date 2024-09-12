def NOD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
total_distance = 0
points = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]
    total_distance += NOD(abs(x2 - x1), abs(y2 - y1))

print(total_distance)