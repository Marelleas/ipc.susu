a = input().split(chr(92))
b = a[len(a)-1]
if b.count(".") == 0:
    print(b)
else:
    print(b[0:b.find(".")])