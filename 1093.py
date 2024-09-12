from math import *

a = []

def pl(x1, y1, x2, y2, x3, y3):
    a = hypot(x1-x2, y1-y2)
    b = hypot(x1-x3, y1-y3)
    c = hypot(x3-x2, y3-y2)
    if a >= b + c or b >= a + c or c >= a + b:
        return -1
    p = (a + b + c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))

n = int(input())
mnx = -1
for i in range(n):
    x, y = map(int, input().split())
    a.append([x,y])
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            k = pl(a[i][0],a[i][1], a[j][0],a[j][1], a[k][0],a[k][1])
            if mnx < 0  or mnx > 0 and k > 0 and k < mnx:
                mnx = k
print("%.6f" % mnx)