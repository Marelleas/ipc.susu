n = int(input())
s = 0
for k in range(n+1):
    for j in range(k,n+1):
        s += (3*k-j)/2
print("%.6f" % s)