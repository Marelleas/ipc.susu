x, y = map(float, input().split())
if y >= 0:
    if 1 <= ((x ** 2) + (y ** 2)) <= 4:
        print("%.6f" % 0)
    else:
        print("%.6f" % x)
else:
    print("%.6f" % x)