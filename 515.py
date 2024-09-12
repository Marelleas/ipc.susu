s = input()
a = 97
e = 0
for i in range(len(s)):
    if s[i] > "z" or s[i] < "a":
        if i == len(s)-1:
            e = 1
            break
    else:
        if chr(a) > s[i]:
            print(i+1)
            break
        a = ord(s[i])
    if i == len(s)-1:
        e = 1
if e == 1:
    print(0)