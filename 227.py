def psi(i): return i >= 0 and i < n
def bfs(n, a, b):
    used = [False]*n
    pred = [-1]*n
    s=[a]
    used[a] = True
    while s:
        x = s.pop(0)
        if x == b: break
        for move in [(x + 1) % n, (x * x + 1) % n, (x * x * x + 1) % n]:
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
n, a, b = map(int, input().split())
l, itog2 = bfs(n,a,b)
print(l)
print(*itog2)