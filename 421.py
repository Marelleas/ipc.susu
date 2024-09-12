a, n = map(int, input().split())
b = input().split()
k = 0
for i in range(n):
    if int(b[i]) == a:
        k = i + 1
        break
print(k)