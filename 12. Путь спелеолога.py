from collections import deque
a = []
n = int(input())
for k in range(n):
    s=input()
    m=[list(input()) for i in range(n)]
    a.append(m)
used=[[[-1]*n for i in range(n)] for j in range(n)]
startk=-1
starti=-1
startj=-1
INF=1e9+7
for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[k][i][j]=='#':
                used[k][i][j]=INF
            if a[k][i][j]=='S':
                startk=k
                starti=i
                startj=j
smartk=[0,0,0,0,-1,1]
smarti=[-1,0,0,1,0,0]
smartj=[0,1,-1,0,0,0]

def bfs(kt,it,jt):
    q=deque()
    q.append((kt,it,jt))
    used[kt][it][jt]=0
    while len(q):
        vk,vi,vj=q.popleft()
        for p in range(6):
            toi=vi+smarti[p]
            tok=vk+smartk[p]
            toj=vj+smartj[p]
            if -1<toi<n and -1<toj<n and -1<tok<n:
                if used[tok][toi][toj]==-1:
                    used[tok][toi][toj]=used[vk][vi][vj]+1
                    q.append((tok,toi,toj))


bfs(startk,starti,startj)
put=INF
for i in range(n):
    for j in range(n):
        if 0< used[0][i][j]<put:
            put = used[0][i][j]
print(put)