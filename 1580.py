from heapq import *
n, m = map(int, input().split())
d = [-int(x) for x in input().split()]
heapify(d)
for i in range(m):
    heapreplace(d, int(d[0]/10))
print(-sum(d))