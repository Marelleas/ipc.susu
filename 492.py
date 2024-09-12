s = input()
ans = ''
contr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in range(len(s)):
    if s[i] in contr:
        ans += s[i]
print(ans)