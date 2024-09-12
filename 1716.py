n = int(input())
put = [-1] * 100100 * 1
q = [1]
put[1] = 0
while len(q):
    v = q.pop(0)
    for i in range(1, int(v ** 0.5) + 2):
        if v % i == 0:
            if v + i <= n and put[v + i] == -1:
                q.append(v + i)
                put[v + i] = put[v] + 1
            if v + v // i <= n and put[v + v // i] == -1:
                q.append(v + v // i)
                put[v + v // i] = put[v] + 1
print(put[n])