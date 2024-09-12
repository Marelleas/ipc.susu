n, k = map(int, input().split())
A = []
for i in range(n):
    A.append(int(input()))

l, r = 1, 10**9
while l < r:
   m = (l + r) // 2
   an = sum(a // m for a in A)
   if an >= k:
       l = m + 1
   else:
       r = m

print(l - 1)