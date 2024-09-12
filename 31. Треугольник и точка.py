def F(x1, y1, x2, y2, x3, y3, x, y):
    A = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    A1 = 0.5 * abs(x * (y2 - y3) + x2 * (y3 - y) + x3 * (y - y2))
    A2 = 0.5 * abs(x1 * (y - y3) + x * (y3 - y1) + x3 * (y1 - y))
    A3 = 0.5 * abs(x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2))

    return abs(A - (A1 + A2 + A3))


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x, y = map(int, input().split())

if F(x1, y1, x2, y2, x3, y3, x, y):
    print("Out")
else:
    print("In")