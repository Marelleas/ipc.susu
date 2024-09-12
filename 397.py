a = input().split()
b = [int(a[0]), int(a[1]), int(a[2]), int(a[3])]
c = sorted(b)
for i in range(len(b)):
    print(c[i], end = " ")