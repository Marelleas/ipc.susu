s = input()
s0 = input()
a = len(s0)
ans = ""
while len(s) >= a:
    if s[:a] == s0:
        s = s[a:]
    else:
        ans += s[0]
        s = s[1:]
print(ans + s)