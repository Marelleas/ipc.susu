a = input()
for i in range(len(a)):
    if a[i] == ":":
        print(a[i])
        break
    else:
        print(a[i], end = "")