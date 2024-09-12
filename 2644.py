n = int(input())
a = input().split()
min = float(a[0])
for i in range(n):
    if float(a[i]) < min:
        min = float(a[i])
print(min)
for j in range(n-1):
    print("%.2f" % (float(a[j])-min), end = " ")
print("%.2f" % (float(a[n-1])-min))