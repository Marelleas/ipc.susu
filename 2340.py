def psi(i): return i >= 0 and i < n
def obritog(itog):
    ans = ''
    for i in range(len(itog)-1):
        if itog[i] // 2 == itog[i+1]:
            ans += '2'
        elif (itog[i] * 3) % 101111 == itog[i + 1]:
            ans += '3'
        elif (itog[i] + 5) % 101111 == itog[i + 1]:
            ans += '5'
        else: ans += '7'
    return ans
def bfs(n, a, b):
    used = [False]*n
    pred = [-1]*n
    s=[a]
    used[a] = True
    while s:
        x = s.pop(0)
        if x == b: break
        for move in [(x//2), (x*3) % n, (x+5) % n, (x-7)%n]:
            if psi(move) and not used[move]:
                s.append(move)
                used[move] = True
                pred[move] = x
    if not used[b]:
        return -1, []
    it1 = [b]
    while pred[b] != -1:
        b = pred[b]
        it1.append(b)
    it1.reverse()
    return len(it1) - 1, it1
a, b = map(int, input().split())
n = 101111
l, itog2 = bfs(n,a,b)
print(l)
print(obritog(itog2))