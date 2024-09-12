n = int(input())
a = input().split()
k = 0
i = 0
for i in range(n):
    if int(a[i]) % 2 != 0:
        k +=1
print(k)