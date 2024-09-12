g, x = map(float, input().split())
g = int(g)
s = 0
for k in range(1, g+1):
    for m in range(k,g+1):
        s += (x+k)/m
print("%.6f" % s)