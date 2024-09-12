s = input().split(".")
answer = []
for i in range(len(s) - 1):
    st = s[i].split()
    for j in range(len(st)-1, -1, -1):
        sr = st[j]
        if len(st) - j == len(st):
            sr += "."
        answer.append(sr)
print(*answer)