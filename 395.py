x, y = map(float, input().split())
if (x**2 + y**2 <= 1) and (y >= abs(x)):
    print("%.6f" % abs((x**2)-1)**0.5)
else:
    print("%.6f" % (x+y))