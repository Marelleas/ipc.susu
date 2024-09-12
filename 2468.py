n = int(input())
a = list(map(int, input().split()))
mx = 0
mxv = 0
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c += 1
        if c > mx:
            mx = c
            mxv = a[i]
        elif c == mx and a[i] > mxv:
            mxv = a[i]
print(mxv)