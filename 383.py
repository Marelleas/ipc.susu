x, y, = map(float, input().split())
if abs(x) + abs(y) <= 1:
    print("Yes")
else:
    print("No")