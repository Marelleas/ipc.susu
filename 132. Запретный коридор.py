n = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
c = []
for i in range(n):
    c.append(a1[i]+a2[i])
    res1 = min(c)
c = []
for i in range(n):
    c.append(a1[i]+a2[-(1+i)])
    res2 = min(c)
print(max(res1,res2))