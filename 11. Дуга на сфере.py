import math


def haversine(x1, y1, x2, y2, radius):
    x1 = math.radians(x1)
    y1 = math.radians(y1)
    x2 = math.radians(x2)
    y2 = math.radians(y2)
    dx = x2-x1
    dy = y2-y1
    a = math.sin(dx / 2) ** 2 + math.cos(x1) * math.cos(x2) * math.sin(dy / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance


R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
min_length = haversine(x1, y1, x2, y2, R)

print("%.2f" % min_length)