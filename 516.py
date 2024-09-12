s = input()
st1 = "("
st2 = ")"
a = []
p = 0
for c in s:
    p += 1
    if c in st1:
        a.append(c)
    elif c in st2:
        if len(a) < 1:
            print(p)
            exit()
        x = a.pop()
        if x == "(" and c != ")":
            print(p)
            exit()
if len(a) < 1:
    print(0)
else:
    print(-1)