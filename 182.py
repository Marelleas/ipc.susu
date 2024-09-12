def istreug(a,b,c):
    return a+b>c and a+c>b and c+b>a
def pl_tr(a,b,c):
    if not istreug(a, b, c):
        return 0
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s
n = int(input())
mas = list(map(int, input().split()))
smx = 0
for i in range(n-2):
    for j in range(i+1,n - 1):
        for k in range(j + 1, n):
            a = mas[i]
            b = mas[j]
            c = mas[k]
            s = pl_tr(a,b,c)
            if s > smx:
                smx = s
print("%.3f" % smx)