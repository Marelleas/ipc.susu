n = int(input())
ans = []
mas = list(map(int, input().split()))
for i in range(n):
    flag = 0
    for j in range(n):
        if i != j:
            if mas[i] % mas[j] == 0:
                flag = 1
                break
    if flag == 0:
        ans.append(mas[i])
print(*ans)