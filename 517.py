strok = input()
strok1 = "([{"
strok2 = ")]}"
a = []
p = 0
for c in strok:
    p += 1
    if c in strok1:
        a.append(c)
    elif c in strok2:
        if len(a) < 1:
            print(p)
            exit()
        x = a.pop()
        if (x == "(" and c != ")") or (x == "[" and c != "]") or (x == "{" and c != "}"):
            print(p)
            exit()
if len(a) < 1:
    print(0)
else:
    print(-1)