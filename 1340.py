n = int(input())
a = list(range(n, 0, -1))
b = []
c = []
bfinish = []
for i in range(n):
    bfinish.append(int(input()))
bfinish.reverse()
n = 0
while True:
    if len(a) != 0 and a[-1] == bfinish[len(b)]:
        b.append(a.pop())
        n += 1
    elif len(c) != 0 and c[-1] == bfinish[len(b)]:
        b.append(c.pop())
        n += 1
    else:
        c.append(a.pop())
        n += 1
    if len(a) == 0 and len(c) == 0:
        break
    if len(a) == 0 and c[-1] != bfinish[len(b)]:
        n = 0
        break
print(n)