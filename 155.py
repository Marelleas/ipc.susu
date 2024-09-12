s = input().split()
answer = []
lg = "aeiouy"
for i in range(len(s)):
    ls = s[i]
    if i >= 1:
        ls = ls.capitalize()
    if len(ls) <= 3:
        answer.append(ls)
    else:
        la = ''
        for j in range(len(ls)):
            if ls[j] in lg and j != 0:
                continue
            else:
                la += ls[j]
        if len(la) <= 3:
            answer.append(la)
        else:
            answer.append(la[0:3])
print(''.join(answer))
