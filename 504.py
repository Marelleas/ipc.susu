a = input()
s = 0
for i in range(len(a)):
    s += int(a[len(a)-1-i])*2**i
print(s)