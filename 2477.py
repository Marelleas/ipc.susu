def q_sort(a, mod):
    if len(a) == 1:
        return a
    M = a[0]
    low = []
    mid = [M]
    hig = []
    for i in range(1, len(a)):
        if a[i] < M:
            low.append(a[i])
        elif a[i] == M:
            mid.append(a[i])
        else:
            hig.append(a[i])
        if mod == 1:
            return q_sort(low, 1) + mid + q_sort(hig, 1)
        else:
            return q_sort(hig, -1) + mid + q_sort(low, -1)
def bubblesort(a):
    f = True
    l = len(a)
    while f:
        f = False
        for i in range(l-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                f = True
        return a
def sort_strange(a):
    l = []
    m = []
    r = []
    for i in range(len(a)):
        if a[i] > 0:
            l.append(a[i])
        elif a[i] == 0:
            m.append(a[i])
        else:
            r.append(a[i])
    return l + m + r
n = int(input())
a = list(map(int, input().split()))
a = sort_strange(a)
for i in range(len(a)):
    print(a[i], end = " ")
