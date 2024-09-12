s = input()
s1 = input()
s2 = input()
a = len(s1)
ans = ""
while len(s) >= a:
    if s[:a] == s1:
        ans += s2
        s = s[a:]
    else:
        ans += s[0]
        s = s[1:]
print(ans + s)