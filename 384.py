x, y = map(float, input().split())
if 2* abs(x) + abs(y) <= 1:
    print("Yes")
else:
    print("No")