a = input()
np = 0
nz = 0
for i in range(len(a)):
    if a[i] == "+":
        np += 1
    elif a[i] == "*":
        nz += 1
print(np, nz)