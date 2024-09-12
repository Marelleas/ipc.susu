s = input()
k = 0
for i in range(len(s)):
    if s[i:i+3] == 'abc':
        k += 1
print(k)