def rast(x1, y1, x2, y2):
    return (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

def r(x1, y1, x2, y2, x3, y3):
    a = rast(x1, y1, x2, y2)
    b = rast(x1, y1, x3, y3)
    c = rast(x2, y2, x3, y3)
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


def mx(x1, y1, x2, y2, x3, y3):
    a = rast(x1, y1, x2, y2)
    b = rast(x1, y1, x3, y3)
    c = rast(x2, y2, x3, y3)
    m = max(a, b, c)
    l = r(x1, y1, x2, y2, x3, y3)
    if m/2 < l*2/m:
        return a*b*c/(4*l)
    else:
        return m/2

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


print("%.2f"%mx(x1, y1, x2, y2, x3, y3))