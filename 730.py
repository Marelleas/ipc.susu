from sys import stdin, stdout
stdin.reconfigure(encoding='cp1251')
stdout.reconfigure(encoding='cp1251')

k = 0

nic = input() + ":"
s = stdin.readlines()

for i in range(len(s)):
	if s[i][0:len(nic)] == nic:
		k += 1
print(k)