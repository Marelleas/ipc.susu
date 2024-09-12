from heapq import *
n, k = map(int, input().split())
sokrov = list(map(int, input().split()))
bednyaki = [[0, i, 0] for i in range(1, k+1)]
heapify(bednyaki)
for i in range(n):
    tekbed = bednyaki[0]
    tekbed[0] = tekbed[0] + sokrov[i]
    tekbed[2] = tekbed[2] + 1
    heapreplace(bednyaki, tekbed)
bednyaki.sort(key = lambda x: x[1])
for i in bednyaki:
    print(i[2], i[0])