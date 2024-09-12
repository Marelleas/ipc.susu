N, R = map(float, input().split())
N = int(N)
a = list(map(float, input().split()))
c = 0
for i in range(N-1):
    if a[i]**2 + a[i+1]**2 <= R**2:
        c += 1
if a[-1]**2 + a[1]**2 <= R**2:
        c += 1
print(c)