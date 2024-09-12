a, b = map(str, input().split())
ce = int(a, 16)
d = int(b, 16)
e = ce+d
f = str(hex(e))
j = f[2: len(f)]
print(j.upper())