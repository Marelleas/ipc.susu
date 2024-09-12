n = int(input())
b = []
for i in range(n):
    b.append(input())
l = sorted(b, key = len)
for i in range(len(l)):
    print(l[i])