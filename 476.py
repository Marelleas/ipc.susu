a = input()
k = 0
i = 0
while i < len(a):
    if a[i] == ":":
        k += 1
        i += 1
    if k == 1:
        print(a[i], end = "")
    elif k == 2:
        break
    i += 1