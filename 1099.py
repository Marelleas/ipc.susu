v = int(input())
cou = 0
for i in range(v+1):
    for j in range(v+1):
        for k in range(v+1):
            if i*j*k == v:
                cou += 1
print(cou)