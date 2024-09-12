
n = int(input())
a = input().split()
max = float(a[0])
for i in range(n):
    if float(a[i]) > max:
        max = float(a[i])
if abs(max) > 1:
    print("Yes")
else:
    print("No")