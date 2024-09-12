n = int(input())
lis = []
s1 =0
s2 =0
for i in range(n):
	it = int(input())
	lis.append(it)
	if i == 0:
		s1 += it ** 2
	else:
		s2 += it
ma = s1*s2

for i in range(1, len(lis)):
	s2 -= int(lis[i])
	s1 += int(lis[i]) ** 2
	if ma < s1*s2:
		ma = s1 * s2
print(ma)