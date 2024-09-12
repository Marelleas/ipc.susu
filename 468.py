s = input()
ans = ""
lc = 0
for i in range(len(s)):
    if lc == 2 and s[i] != ".":
        ans += "."
    if s[i] != ".":
        ans += s[i]
        lc = 0
    else:
        if lc < 3:
            ans += s[i]
            lc += 1
print(ans)