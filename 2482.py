n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(m):
    no = 101
    nd = 101
    for j in range(n):
        if a[j][i] < 0:
            no = j
            break
    for t in range(n - 1, 0, -1):
        if a[t][i] > 0 and t != no:
            nd = t
            break
    if no != 101 and nd != 101:
        a[no][i], a[nd][i] = a[nd][i], a[no][i]
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))