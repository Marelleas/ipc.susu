n = int(input())
sum = 0
for k in range(1, n+1):
    for m in range(1, n+1):
        sum += (n/(2*k+m))
print("%.6f" % sum)