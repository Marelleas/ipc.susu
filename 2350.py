from sys import stdin
s = ''
ls = "?.!"
for i in stdin.readlines():
    s += i
k = 0
tu = True
for i in s[1:]:
    if i.isupper():
        if tu:
            k += 1
        else:
            tu = True
    elif i in ls:
        tu = False
print(k)