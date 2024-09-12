w, h, n = map(int, input().split())
sn = int(n**0.5) + 1
s = (w + h) * n
for k in range(1, sn+1):
    m = (n + k - 1) // k
    s = min(s, max(k * w, m * h))
    s = min(s, max(m * w, k * h))
print(s)