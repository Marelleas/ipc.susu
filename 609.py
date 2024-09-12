p = float(input())
s = 1000
n = 0
while n > -1:
    n += 1
    s += s*p/100
    if s > 1100:
        break
print(n, end=" ")
print("%.6f" % s)