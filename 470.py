a = input()
k = 0
for i in range(len(a)-1):
    if a[i] == "a" and a[i+1] == "a":
        k += 1
        break
if k == 0:
    print(k)
else:
    print(i+1)