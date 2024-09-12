m, n = map(int, input().split())
lis = []
for i in range(1, m):
	if (i * n) % m == 0:
		lis.append(i * n)
if len(lis) == 0:
	print(0)
else:
	print(*lis)