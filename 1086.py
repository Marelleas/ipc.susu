m,n = map(int, input().split())
f = 0
for i in range(11):
    for j in range(21):
        for l in range(201):
            if (i*10 + j*5 + l*0.5 == m) and (i + j + l == n):
                f += 1
if f == 0:
    print("no")
else:
    print("yes")