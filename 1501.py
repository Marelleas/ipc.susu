n = int(input())
a = list(range(1, n+1))
b = []
c = []
bstart = list(map(int, input().split()))
bstart.reverse()
n = 0
while True:
    if len(bstart) != 0 and bstart[-1] == a[len(b)]:
        b.append(bstart.pop(-1))
        n += 1
    elif len(c) != 0 and c[0] == a[len(b)]:
        b.append(c.pop(0))
        n += 1
    else:
        c.append(bstart.pop(-1))
        n += 1
    if len(bstart) == 0 and len(c) == 0:
        break
    if len(bstart) == 0 and c[0] != a[len(b)]:
        n = 0
        break
if n == 0:
    print("NO")
else:
    print("YES")