x, y = map(float, input().split())
if (y <= (1 - x ** 2)) and (x**2 + (y-1)**2 <= 1):
    print("%.6f" % (x - y))
else:
    print("%.6f" % (x * y + 7))