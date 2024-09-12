n = int(input())
k = 0
for i in range(n+1):
    for j in range(i, n+1):
        k += (((-1)**i)*j)/n
print("%.6f" % k)