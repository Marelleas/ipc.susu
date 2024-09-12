def prt(a):
    for row in a:
        for x in row:
            print(x, end="")
        print()

n = int(input())
m = [ list(input()) for i in range(n) ]
used = [ [-1] * n for i in range(n) ]
pr = [ [(-1, -1)] * n for i in range(n) ]

starti = -1
startj = -1
endi = -1
endj = -1
inf = 1e9 + 7
for i in range(n):
    for j in range(n):
        if m[i][j] == "O":
            used[i][j] = inf
        if m[i][j] == "@":
            starti = i
            startj = j
        if m[i][j] == "X":
            endi = i
            endj = j 
smi = [-1,0,1,0]
smj = [0,1,0,-1]
def bfs(it, jt):
    q = []
    q.append((it, jt))
    used[it][jt] = 0
    while len(q):
        vi, vj = q[0]
        q = q[1:]
        for k in range(4):
            toi = vi + smi[k]
            toj = vj + smj[k]
            if -1 < toi < n and -1 < toj < n:
                if used[toi][toj] == -1:
                    used[toi][toj] = used[vi][vj] + 1
                    q.append((toi, toj))
                    pr[toi][toj] = (vi,vj)

bfs(starti, startj)

if used[endi][endj] == -1:
    print("N")
else:
    print("Y")
    vi = endi
    vj = endj
    while (vi,vj) != (starti, startj):
        m[vi][vj] = "+"
        vi,vj = pr[vi][vj]
    for i in range(n):
        for j in range(n):
            print(m[i][j], end = "")
        print()